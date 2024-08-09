from django.contrib import admin
from .models import TimeScale

class TimeScaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'program_progress_percentage', 'time_program_progress_percentage', 'date', 'create_date')

admin.site.register(TimeScale, TimeScaleAdmin)