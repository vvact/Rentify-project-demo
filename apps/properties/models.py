import random
import string

from autoslug import AutoSlugField
from django.core.validators import MinValueValidator
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class PropertyPublishedManager(models.Manager):
    def get_queryset(self):
        return super(PropertyPublishedManager, self).get_queryset().filter(published=True)

class Property(TimeStampedUUIDModel):
    class AdvertType(models.TextChoices):
        FOR_SALE = 'SALE', _('Sale')
        FOR_RENT = 'RENT', _('Rent')
        AUCTION = 'AUCTION', _('Auction')

    class PropertyType(models.TextChoices):
        SINGLE_ROOM = 'Single_Room', _('Single Room')
        DOUBLE_ROOM = 'Double_Room', _('Double Room')
        BEDSITTER = 'Bedsitter', _('Bedsitter')
        ONE_BEDROOM = 'One_Bedroom',_('One Bedroom')
        TWO_BEDROOM = 'Two_Bedroom',_('Two Bedroom')
        THREE_BEDROOM = 'Three_Bedroom',_('Three Bedroom')
        APARTMENT = 'APARTMENT', _('Apartment')
        HOUSE = 'HOUSE', _('House')
        LAND = 'LAND', _('Land')
        OFFICE = 'Office',_('Office')
        STUDIO_APARTMENT = 'STUDIO_APARTMENT', _('Studio Apartment')
        WAREHOUSE = 'Warehouse', _('Warehouse')
        VILLA = 'VILLA', _('Villa')
        COMMERCIAL = 'Commercial',_('Commercial')
        FLAT = 'FLAT', _('Flat')
        BUNGALOW = 'BUNGALOW', _('Bungalow')
        PENTHOUSE = 'PENTHOUSE', _('Penthouse')
        OTHER = 'Other', _('Other')

    user = models.ForeignKey(User, verbose_name=_("Agent, Renter, Seller or Buyer"), related_name='agent_buyer', on_delete=models.DO_NOTHING)
    title = models.CharField(verbose_name=_('Property Title'), max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)
    ref_code = models.CharField(verbose_name=_("Property Reference Code"), max_length=300, unique=True, blank=True)
    description = models.TextField(verbose_name=_("Description"), default="Default Description...Update description please...")
    country = CountryField(verbose_name=_('Country'), default="KE", blank_label="(select Country)")
    city = models.CharField(verbose_name=_('City'), max_length=200, default="Nairobi")
    postal_code = models.CharField(verbose_name=_("Postal Code"), max_length=100, default=150)
    street_address = models.CharField(verbose_name=_('Street Address'), max_length=200, default="KMT Avenue")
    property_number = models.IntegerField(verbose_name=_("Property Number"), validators=[MinValueValidator(0)], default=120)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2, default=0.0)
    tax = models.DecimalField(verbose_name=_("Property Tax"), max_digits=8, decimal_places=2, default=0.0, help_text=_("Property Tax"))
    plot_area = models.DecimalField(verbose_name=_("Plot Area(m^2)"), max_digits=8, decimal_places=2, default=0.0, help_text=_("Plot Area"))
    total_floors = models.IntegerField(verbose_name=_("Total Floors"), validators=[MinValueValidator(0)], default=1, help_text=_("Total Floors"))
    bedroom = models.IntegerField(verbose_name=_("Bedroom"), validators=[MinValueValidator(0)], default=1, help_text=_("Bedroom"))
    bathroom = models.IntegerField(verbose_name=_("Bathroom"), validators=[MinValueValidator(0)], default=1, help_text=_("Bathroom"))
    garage = models.IntegerField(verbose_name=_("Garage"), validators=[MinValueValidator(0)], default=1, help_text=_("Garage"))
    furnished = models.BooleanField(verbose_name=_("Furnished"), default=False, help_text=_("Furnished"))
    swimming_pool = models.BooleanField(verbose_name=_("Swimming Pool"), default=False, help_text=_("Swimming Pool"))
    advert_type = models.CharField(verbose_name=_("Advert Type"), max_length=10, choices=AdvertType.choices, default=AdvertType.FOR_SALE)
    property_type = models.CharField(verbose_name=_("Property Type"), max_length=40, choices=PropertyType.choices, default=PropertyType.SINGLE_ROOM)
    cover_photo = models.ImageField(verbose_name=_("Main Photo"), upload_to="property/cover_photo", blank=True, null=True, default="/cover_photo.jpg")
    photo1 = models.ImageField(verbose_name=_("Photo 1"), upload_to="property/photo1", default="/interior_sample.jpg", blank=True)
    photo2 = models.ImageField(verbose_name=_("Photo 2"), upload_to="property/photo2", default="/interior_sample.jpg", blank=True)
    photo3 = models.ImageField(verbose_name=_("Photo 3"), upload_to="property/photo3", default="/interior_sample.jpg", blank=True)
    photo4 = models.ImageField(verbose_name=_("Photo 4"), upload_to="property/photo4", default="/interior_sample.jpg", blank=True)
    published_status = models.BooleanField(verbose_name=_("Published Status"), default=False)
    views = models.IntegerField(verbose_name=_("Views"), default=0)

    objects = models.Manager()
    published = PropertyPublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")

    def save(self, *args, **kwargs):
        if not self.ref_code:
            self.ref_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        self.title = self.title.title()
        self.description = self.description.capitalize()
        super(Property, self).save(*args, **kwargs)

    @property
    def final_property_price(self):
        tax_percentage = self.tax
        property_price = self.price
        tax_amount = property_price * (tax_percentage / 100)
        final_property_price = property_price + tax_amount
        return round(final_property_price, 2)

class PropertyViews(TimeStampedUUIDModel):
    ip = models.CharField(verbose_name=_("IP Address"), max_length=260, default="127.0.0.1")
    property = models.ForeignKey(Property, related_name='property_views', verbose_name=_("Property"), on_delete=models.CASCADE)

    def __str__(self):
        return f"Total views on - {self.property.title} is - {self.property.views} view(s)"

    class Meta:
        verbose_name = _("Views on Property")
        verbose_name_plural = _("Total Property Views")
