import random
import string


from autoslug import AutoSlugField
from django.contrib.auth import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries import CountryField
from apps.common.models import TimeStampedUUIDModel


User = get_user_model()


class PropertyPublishedManager(models.Manager):
    def get_queryset(self):
        return super(PropertyPublishedManager, self).get_queryset().filter(published=True)
