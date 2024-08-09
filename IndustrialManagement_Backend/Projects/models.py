from django.db import models
from SubOrganizations.models import SubOrganization, CustomUser

class Project(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(unique=True, max_length=50)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    real_start_date = models.DateTimeField(blank=True, null=True)
    real_end_date = models.DateTimeField(blank=True, null=True)
    external_members = models.TextField(max_length=500, blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subOrganization = models.ForeignKey(SubOrganization, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name