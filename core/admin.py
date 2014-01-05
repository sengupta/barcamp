from django.contrib import admin
from .models import Camp, UserProfile, Session

class CampAdmin(admin.ModelAdmin):
    pass

class UserProfileAdmin(admin.ModelAdmin):
    pass

class SessionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Camp, CampAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Session, SessionAdmin)
