from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from .models import Property, PropertyViews
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        fields = "__all__"

    def get_user(self, obj):
        return obj.user.username


class PropertyCREATESerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        exclude = ["updated_at" "pkid"]


class PropertyViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyViews
        exclude = ["updated_at", "pkid"]
