from django.contrib import admin
from .models import Camp, UserProfile, Session

class CampAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'start',
            'end',
            'slug',
            )

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
            'user',
            'name',
            )

class SessionAdmin(admin.ModelAdmin):
    list_display = (
            'title',
            'speaker',
            'camp',
            'enabled',
            'slug',
            )

admin.site.register(Camp, CampAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Session, SessionAdmin)
