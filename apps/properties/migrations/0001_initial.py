# Generated by Django 5.0.6 on 2024-05-28 23:21

import autoslug.fields
import django.core.validators
import django.db.models.deletion
import django_countries.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "title",
                    models.CharField(max_length=250, verbose_name="Property Title"),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        always_update=True,
                        editable=False,
                        populate_from="title",
                        unique=True,
                    ),
                ),
                (
                    "ref_code",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        unique=True,
                        verbose_name="Property Reference Code",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        default="Default Description...Update description please...",
                        verbose_name="Description",
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        default="KE", max_length=2, verbose_name="Country"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        default="Nairobi", max_length=200, verbose_name="City"
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        default=150, max_length=100, verbose_name="Postal Code"
                    ),
                ),
                (
                    "street_address",
                    models.CharField(
                        default="KMT Avenue",
                        max_length=200,
                        verbose_name="Street Address",
                    ),
                ),
                (
                    "property_number",
                    models.IntegerField(
                        default=120,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Property Number",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=8,
                        verbose_name="Price",
                    ),
                ),
                (
                    "tax",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        help_text="Property Tax",
                        max_digits=8,
                        verbose_name="Property Tax",
                    ),
                ),
                (
                    "plot_area",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        help_text="Plot Area",
                        max_digits=8,
                        verbose_name="Plot Area(m^2)",
                    ),
                ),
                (
                    "total_floors",
                    models.IntegerField(
                        default=1,
                        help_text="Total Floors",
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Total Floors",
                    ),
                ),
                (
                    "bedroom",
                    models.ImageField(
                        blank=True,
                        default=1,
                        null=True,
                        upload_to="property/bedroom",
                        verbose_name="Bedroom",
                    ),
                ),
                (
                    "bathroom",
                    models.ImageField(
                        blank=True,
                        default=1.0,
                        max_length=4,
                        upload_to="property/bathroom",
                        verbose_name="Bathroom",
                    ),
                ),
                (
                    "advert_type",
                    models.CharField(
                        choices=[
                            ("SALE", "Sale"),
                            ("RENT", "Rent"),
                            ("Auction", "Auction"),
                        ],
                        default="SALE",
                        max_length=10,
                        verbose_name="Advert Type",
                    ),
                ),
                (
                    "property_type",
                    models.CharField(
                        choices=[
                            ("Single_Room", "Single_Room"),
                            ("Double_Room", "Double_Room"),
                            ("Bedsitter", "Bedsitter"),
                            ("One_Bedroom", "One_Bedroom"),
                            ("Two_Bedroom", "Two_Bedroom"),
                            ("Three_Bedroom", "Three_Bedroom"),
                            ("APARTMENT", "Apartment"),
                            ("HOUSE", "House"),
                            ("LAND", "Land"),
                            ("Office", "Office"),
                            ("STUDIO_APARTMENT", "Studio Apartment"),
                            ("Warehouse", "Warehouse"),
                            ("VILLA", "Villa"),
                            ("CONDOMINIUM", "Condominium"),
                            ("Commercial", "Commercial"),
                            ("FLAT", "Flat"),
                            ("BUNGALOW", "Bungalow"),
                            ("PENTHOUSE", "Penthouse"),
                            ("TERRACED_HOUSE", "Terraced House"),
                            ("TERRACED_FLAT", "Terraced Flat"),
                            ("Other", "Other"),
                        ],
                        default="Single_Room",
                        max_length=40,
                        verbose_name="Property Type",
                    ),
                ),
                (
                    "cover_photo",
                    models.ImageField(
                        blank=True,
                        default="/cover_photo.jpg",
                        null=True,
                        upload_to="property/cover_photo",
                        verbose_name="Main Photo",
                    ),
                ),
                (
                    "photo1",
                    models.ImageField(
                        blank=True,
                        default="/interior_sample.jpg",
                        upload_to="property/photo2",
                        verbose_name="Photo 2",
                    ),
                ),
                (
                    "photo2",
                    models.ImageField(
                        blank=True,
                        default="/interior_sample.jpg",
                        upload_to="property/photo3",
                        verbose_name="Photo 3",
                    ),
                ),
                (
                    "photo3",
                    models.ImageField(
                        blank=True,
                        default="/interior_sample.jpg",
                        upload_to="property/photo3",
                        verbose_name="Photo 3",
                    ),
                ),
                (
                    "photo4",
                    models.ImageField(
                        blank=True,
                        default="/interior_sample.jpg",
                        upload_to="property/photo3",
                        verbose_name="Photo 3",
                    ),
                ),
                (
                    "published_status",
                    models.BooleanField(default=False, verbose_name="Published Status"),
                ),
                ("views", models.IntegerField(default=0, verbose_name="Views")),
            ],
            options={
                "verbose_name": "Property",
                "verbose_name_plural": "Properties",
            },
        ),
        migrations.CreateModel(
            name="PropertyViews",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ip",
                    models.CharField(
                        default="127.0.0.1", max_length=260, verbose_name="IP Address"
                    ),
                ),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_views",
                        to="properties.property",
                        verbose_name="Property",
                    ),
                ),
            ],
            options={
                "verbose_name": " Views on Property",
                "verbose_name_plural": " Total Property Views",
            },
        ),
    ]
