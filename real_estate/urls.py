from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from djoser.views import TokenCreateView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("mademen/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profile/", include("apps.profiles.urls")),
    path("api/v1/properties/" , include("apps.properties.urls")),
    path("api/v1/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/v1/auth/token/create/", TokenCreateView.as_view(), name="token_create"),
    path("api/vi/rating/", include("apps.ratings.urls")),
    path("api/v1/enquiries/",include("apps.enquiries.urls"))
]

admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real Estate Admin Portal"
admin.site.index_title = "Welcome to the Real Estate Portal"