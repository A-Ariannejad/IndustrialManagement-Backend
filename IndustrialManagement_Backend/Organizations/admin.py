from django.contrib import admin
from .models import Organization

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nickname', 'phone_number', 'postal_code', 'owner', 'create_date')

admin.site.register(Organization, OrganizationAdmin)