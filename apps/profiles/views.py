from  rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import ProfileNotFound,NotYourProfile

from .models import Profile
from .renderers import ProfileJSONREnderer
from  .serializers import ProfileSerializer, UpdateProfileSerializer