from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'create_date')

admin.site.register(CustomUser, CustomUserAdmin)