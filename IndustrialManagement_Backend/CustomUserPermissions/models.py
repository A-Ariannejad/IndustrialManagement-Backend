from django.db import models

class CustomUserPermission(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    add_subOrganization = models.BooleanField(default=False)
    add_manager = models.BooleanField(default=False)
    add_project = models.BooleanField(default=False)
    user_access = models.BooleanField(default=False)