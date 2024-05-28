from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel


class Enquiry(TimeStampedUUIDModel):
    """
    User model
    """
    name = models.CharField(
        max_length=255,
        verbose_name=_("Your Name"),
    )
    phone_number = PhoneNumberField(
        verbose_name=_("Your Phone"),
    )
    email = models.EmailField(
        max_length=255,
        verbose_name=_("Your Email"),
    )
    subject = models.CharField(
        max_length=255,
        verbose_name=_("Subject"),
    )
    message = models.TextField(
        verbose_name=_("Message"),
    )

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = _("Enquiry")
        verbose_name_plural = _("Enquiries")
