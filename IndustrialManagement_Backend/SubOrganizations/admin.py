from django.contrib import admin
from .models import SubOrganization

class SubOrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nickname', 'phone_number', 'postal_code', 'owner', 'organization', 'create_date')

admin.site.register(SubOrganization, SubOrganizationAdmin)