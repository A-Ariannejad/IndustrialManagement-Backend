from django.contrib import admin
from .models import PieScale

class PieScaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'pending_percentage', 'doing_percentage', 'finished_percentage', 'date', 'create_date')

admin.site.register(PieScale, PieScaleAdmin)