from rest_framework import serializers
from .models import CustomUser
from CustomUserPermissions.serializers import PermissionSerializer

class GetCustomUserSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'user_permissions']

class GetCustomUserProfileSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'create_date', 'user_permissions']

class CreateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','email', 'password', 'first_name', 'last_name', 'create_date', 'user_permissions']
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        permissions = instance.user_permissions
        ret['user_permissions'] = PermissionSerializer(permissions).data
        return ret