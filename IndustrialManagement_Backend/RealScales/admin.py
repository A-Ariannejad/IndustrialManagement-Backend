from django.contrib import admin
from .models import RealScale

class RealScaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'program_progress_percentage', 'real_program_progress_percentage', 'date', 'create_date')

admin.site.register(RealScale, RealScaleAdmin)