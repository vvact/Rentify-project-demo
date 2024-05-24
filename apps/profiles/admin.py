from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','pkid','user','gender','phone_number','country','city']
    list_display_links = ['id','pkid','user','gender','phone_number','country','city']
    list_filter = ['gender','phone_number','country','city']


admin.site.register(Profile, ProfileAdmin)