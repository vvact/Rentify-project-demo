import logging

import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import PropertyNotFound
from .models import Property, PropertyViews
from .pagination import PropertyPagination
from .serializers import (
    PropertySerializer,
    PropertyCREATESerializer,
    PropertyViewsSerializer
)

logger = logging.getLogger(__name__)

class PropertyFilter(django_filters.FilterSet):
    advert_type = django_filters.CharFilter(field_name="advert_type", lookup_expr="iexact")
    property_type = django_filters.CharFilter(field_name="property_type", lookup_expr="iexact")
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price__lt = django_filters.NumberFilter(field_name="price", lookup_expr="lt")

    class Meta:
        model = Property
        fields = ["advert_type", "property_type", "price"]

class ListAllPropertiesAPIView(generics.ListAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all().order_by('created_at')
    pagination_class = PropertyPagination  # Corrected
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = PropertyFilter
    search_fields = ['country', 'city']  # Corrected
    ordering_fields = ['created_at']

class ListAgentPropertyAPIView(generics.ListAPIView):
    serializer_class = PropertySerializer
    pagination_class = PropertyPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = PropertyFilter
    search_fields = ['country', 'city']  # Corrected
    ordering_fields = ['created_at']  # Corrected

    def get_queryset(self):
        user = self.request.user
        return Property.objects.filter(user=user).order_by('created_at')

class PropertyViewsAPIView(generics.ListAPIView):
    serializer_class = PropertyViewsSerializer
    queryset = PropertyViews.objects.all()

class PropertyDetailView(APIView):
    def get(self, request, slug):  # Corrected
        try:
            property = Property.objects.get(slug=slug)
        except Property.DoesNotExist:
            raise PropertyNotFound

        x_forwarded_for = request.META.get('HTTP_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        if not PropertyViews.objects.filter(property=property, ip=ip).exists():
            PropertyViews.objects.create(property=property, ip=ip)
            property.views += 1
            property.save()  # Corrected

        serializer = PropertySerializer(property, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_property_api_view(request, slug):
    try:
        property = Property.objects.get(slug=slug)
    except Property.DoesNotExist:
        raise PropertyNotFound

    if property.user != request.user:
        return Response(
            {"error": "You can't update a property that doesn't belong to you"},
            status=status.HTTP_403_FORBIDDEN
        )

    if request.method == 'PUT':
        serializer = PropertySerializer(property, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # Corrected
def create_property_api_view(request):
    user = request.user  # Corrected
    data = request.data
    data['user'] = request.user.pkid
    serializer = PropertyCREATESerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        logger.info(f"Property {serializer.data.get('title')} created by {user.username}")
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_property_api_view(request, slug):
    try:
        property = Property.objects.get(slug=slug)
    except Property.DoesNotExist:
        raise PropertyNotFound

    if property.user != request.user:
        return Response(
            {"error": "You can't delete a property that doesn't belong to you"},
            status=status.HTTP_403_FORBIDDEN
        )

    if request.method == "DELETE":
        delete_operation = property.delete()
        data = {'success': "Deletion was successful"} if delete_operation else {'failure': 'Deletion failed'}
        return Response(data=data)

@api_view(['POST'])
def upload_property_image(request):
    data = request.data

    try:
        property = Property.objects.get(id=data['property_id'])
    except Property.DoesNotExist:
        raise PropertyNotFound

    property.cover_photo = request.FILES.get("cover_photo")
    property.photo1 = request.FILES.get("photo1")
    property.photo2 = request.FILES.get("photo2")
    property.photo3 = request.FILES.get("photo3")
    property.photo4 = request.FILES.get("photo4")
    property.save()
    return Response("Image(s) uploaded")

class PropertySearchAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PropertySerializer

    def post(self, request):
        queryset = Property.objects.filter(published_status=True)
        data = request.data

        advert_type = data.get('advert_type')
        property_type = data.get('property_type')
        price = data.get('price', '-1')
        bedrooms = data.get('bedrooms', '0+')
        bathrooms = data.get('bathrooms', '0+')
        catch_phrase = data.get('catch_phrase', '')

        if advert_type:
            queryset = queryset.filter(advert_type__iexact=advert_type)
        if property_type:
            queryset = queryset.filter(property_type__iexact=property_type)

        price_map = {
            '$0+': 0,
            '$50,000+': 50000,
            '$100,000+': 100000,
            '$150,000+': 150000,
            '$200,000+': 200000,
            '$250,000+': 250000,
            '$300,000+': 300000,
            '$350,000+': 350000,
            '$400,000+': 4000000,
            'Any': -1
        }
        price = price_map.get(price, -1)
        if price != -1:
            queryset = queryset.filter(price__gte=price)

        bedrooms_map = {
            '0+': 0,
            '1+': 1,
            '2+': 2,
            '3+': 3,
            '4+': 4,
            '5+': 5
        }
        bedrooms = bedrooms_map.get(bedrooms, 0)
        queryset = queryset.filter(bedrooms__gte=bedrooms)

        bathrooms_map = {
            '0+': 0.0,
            '1+': 1.0,
            '2+': 2.0,
            '3+': 3.0
        }
        bathrooms = bathrooms_map.get(bathrooms, 0.0)
        queryset = queryset.filter(bathrooms__gte=bathrooms)

        if catch_phrase:
            queryset = queryset.filter(description__icontains=catch_phrase)

        serializer = PropertySerializer(queryset, many=True)
        return Response(serializer.data)
