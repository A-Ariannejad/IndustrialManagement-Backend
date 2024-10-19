from django import forms
from django.contrib import admin
from .models import Project, CustomUser

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProjectAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.subOrganization:
            sub_organization = self.instance.subOrganization
            self.fields['owner'].queryset = CustomUser.objects.filter(subOrganizations=sub_organization)
        else:
            self.fields['owner'].queryset = CustomUser.objects.none()

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nickname', 'start_date', 'end_date', 'real_start_date', 'real_end_date', 'subOrganization', 'owner', 'create_date')
    form = ProjectAdminForm

admin.site.register(Project, ProjectAdmin)
