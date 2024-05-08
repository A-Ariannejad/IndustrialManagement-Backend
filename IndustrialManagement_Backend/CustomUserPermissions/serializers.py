from rest_framework import serializers
from .models import CustomUserPermission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserPermission
        fields = ['id', 'name', 'add_subOrganization', 'add_manager', 'add_project', 'user_access']
        