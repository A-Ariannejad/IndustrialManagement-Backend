from django.contrib import admin
from .models import ProjectFile

class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'uploader', 'project', 'create_date')

admin.site.register(ProjectFile, ProjectFileAdmin)