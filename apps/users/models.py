from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser,PermissionsMixin):
     pkid = models.BigAutoField(primary_key=True,editable=False)
     id = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
     username = models.CharField(verbose_name=_('Username'), max_length=255, unique=True)
     first_name = models.CharField(validators=_('First Name'), max_length=50)
     last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
