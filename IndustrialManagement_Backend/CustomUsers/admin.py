from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'social_id', 'create_date')

admin.site.register(CustomUser, CustomUserAdmin)