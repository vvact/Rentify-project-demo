# Generated by Django 5.0.6 on 2024-05-28 23:21

import phonenumber_field.modelfields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Enquiry",
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
                ("name", models.CharField(max_length=255, verbose_name="Your Name")),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, verbose_name="Your Phone"
                    ),
                ),
                ("email", models.EmailField(max_length=255, verbose_name="Your Email")),
                ("subject", models.CharField(max_length=255, verbose_name="Subject")),
                ("message", models.TextField(verbose_name="Message")),
            ],
            options={
                "verbose_name": "Enquiry",
                "verbose_name_plural": "Enquiries",
            },
        ),
    ]