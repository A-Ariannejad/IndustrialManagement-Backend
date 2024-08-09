from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nickname', 'start_date', 'end_date', 'real_start_date', 'real_end_date', 'external_members', 'owner', 'subOrganization', 'create_date')

admin.site.register(Project, ProjectAdmin)