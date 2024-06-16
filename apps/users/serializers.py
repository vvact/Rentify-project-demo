from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    gende = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")

    city = serializers.CharField(source="profile.city")
    country = CountryField(source="profile.country")
    profile_photo = serializers.ImageField(source="profile.profile_photo")
    top_seller = serializers.BooleanField(source="profile.top_seller")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField(source="get_full_name")

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "gender",
            "phone_number",
            "city",
            "country",
            "profile_photo",
            "top_seller" "license",
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self, obj):
        return obj.last_name.title()

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)

        if instance.is_superuser:
            representation["admin"] = True
        return representation


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "email", "username", "first_name", "last_name", "password"]
