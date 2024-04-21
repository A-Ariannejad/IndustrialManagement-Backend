from django.db import models

class CustomUserPermission(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    is_controller = models.BooleanField(default=False)
    is_viewer = models.BooleanField(default=False)
    is_calculator = models.BooleanField(default=False)
    is_supporter = models.BooleanField(default=False)