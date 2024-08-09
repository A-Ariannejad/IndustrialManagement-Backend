from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'nickname', 'first_name', 'last_name', 'social_id_number', 'personal_id_number', 'mobile_phone_number',  'phone_number', 'education_level', 'subOrganizations', 'create_date', 'user_permissions']


admin.site.register(CustomUser, CustomUserAdmin)