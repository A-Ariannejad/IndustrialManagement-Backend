from rest_framework import serializers
from .models import CustomUserPermission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserPermission
        fields = ['id', 'name', 'is_controller', 'is_viewer', 'is_calculator', 'is_supporter']
        