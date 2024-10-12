from rest_framework import serializers
from .models import CustomUser, CustomUserPermission
from IndustrialManagement_Backend.serializers import GetPermissionSerializer
from IndustrialManagement_Backend.serializers import GetSubOrganizationSerializer
from SubOrganizations.models import SubOrganization

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
    
class UpdateCustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, allow_null=True)  # Allow blank and null for username
    nickname = serializers.CharField(required=False, allow_blank=True, allow_null=True)  # Allow blank and null for nickname
    education_level = serializers.ChoiceField(choices=CustomUser.EDUCATION_CHOICES, required=False, allow_blank=True)  # Allow blank for education_level
    user_permissions = serializers.PrimaryKeyRelatedField(queryset=CustomUserPermission.objects.all(), required=False, allow_null=True)  # Allow null for user_permissions
    subOrganizations = serializers.PrimaryKeyRelatedField(queryset=SubOrganization.objects.all(), required=False, allow_null=True)  # Allow null for user_permissions
    password = serializers.CharField(required=False, allow_blank=True, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'nickname', 'first_name', 'last_name', 'password', 'social_id_number', 'personal_id_number', 'mobile_phone_number',  'phone_number', 'education_level', 'subOrganizations', 'create_date', 'user_permissions']
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        permissions = instance.user_permissions
        ret['user_permissions'] = GetPermissionSerializer(permissions).data
        return ret