from django.db import models
from CustomUsers.models import CustomUser

class Organization(models.Model):
    name = models.CharField(max_length=50)
    boss = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(max_length=250)
    create_date = models.DateTimeField(auto_now_add=True)
