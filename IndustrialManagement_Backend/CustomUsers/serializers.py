from rest_framework import serializers
from .models import CustomUser
from CustomUserPermissions.serializers import PermissionSerializer

class GetCustomUserSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'user_permissions']

class GetCustomUserProfileSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'nickname', 'first_name', 'last_name', 'social_id_number', 'personal_id_number', 'mobile_phone_number',  'phone_number', 'education_level', 'create_date', 'user_permissions']

class CreateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'nickname', 'first_name', 'last_name', 'social_id_number', 'personal_id_number', 'mobile_phone_number',  'phone_number', 'education_level', 'create_date', 'user_permissions']
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        permissions = instance.user_permissions
        ret['user_permissions'] = PermissionSerializer(permissions).data
        return ret