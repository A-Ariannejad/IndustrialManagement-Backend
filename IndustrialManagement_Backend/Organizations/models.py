from django.db import models
from CustomUsers.models import CustomUser

class Organization(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(unique=True, max_length=50)
    phone_number = models.CharField(max_length=30, blank=True)
    postal_code = models.CharField(max_length=30, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
