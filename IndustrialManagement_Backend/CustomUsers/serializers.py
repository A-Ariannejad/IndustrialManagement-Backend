from rest_framework import serializers
from .models import CustomUser
from IndustrialManagement_Backend.serializers import GetPermissionSerializer
from IndustrialManagement_Backend.serializers import GetSubOrganizationSerializer

class GetCustomUserProfileSerializer(serializers.ModelSerializer):
    user_permissions = GetPermissionSerializer()
    subOrganizations = GetSubOrganizationSerializer()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'nickname', 'first_name', 'last_name', 'social_id_number', 'personal_id_number', 'mobile_phone_number', 'phone_number', 'education_level', 'subOrganizations', 'create_date', 'user_permissions']

class CreateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'nickname', 'first_name', 'password', 'last_name', 'social_id_number', 'personal_id_number', 'mobile_phone_number',  'phone_number', 'education_level', 'subOrganizations', 'create_date', 'user_permissions']
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        permissions = instance.user_permissions
        ret['user_permissions'] = GetPermissionSerializer(permissions).data
        return ret