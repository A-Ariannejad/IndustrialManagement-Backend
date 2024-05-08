from django.contrib import admin
from .models import Organization

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'boss', 'create_date')

admin.site.register(Organization, OrganizationAdmin)