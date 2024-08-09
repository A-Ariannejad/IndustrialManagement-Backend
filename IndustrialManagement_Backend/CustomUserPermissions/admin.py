from django.contrib import admin
from .models import CustomUserPermission

class CustomUserPermissionPerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'add_subOrganization', 'add_manager', 'add_project', 'user_access')

admin.site.register(CustomUserPermission, CustomUserPermissionPerAdmin)