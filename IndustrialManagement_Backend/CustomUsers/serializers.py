from rest_framework import serializers
from .models import CustomUser
from IndustrialManagement_Backend.serializers import GetSubOrganizationSerializer, GetProjectSerializer
from Projects.models import SubOrganization, Project

class GetCustomUserProfileSerializer(serializers.ModelSerializer):
    # subOrganizations = GetSubOrganizationSerializer()
    projects = GetProjectSerializer(many=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'nickname', 'first_name', 'last_name', 'social_id_number', 'personal_id_number', 'mobile_phone_number', 'phone_number', 'education_level', 'admin', 'crud_project', 'is_superuser', 'projects', 'subOrganizations', 'create_date']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['subOrganizations'] = GetSubOrganizationSerializer(instance.subOrganizations, context={'request': self.context['request']}).data
        return ret

class CreateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'nickname', 'first_name', 'password', 'last_name', 'social_id_number', 'personal_id_number', 'mobile_phone_number', 'phone_number', 'education_level', 'admin', 'crud_project', 'is_superuser', 'projects', 'subOrganizations', 'create_date']
    
class UpdateCustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    nickname = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    education_level = serializers.ChoiceField(choices=CustomUser.EDUCATION_CHOICES, required=False, allow_blank=True)
    subOrganizations = serializers.PrimaryKeyRelatedField(queryset=SubOrganization.objects.all(), required=False, allow_null=True)
    projects = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), required=False, allow_null=True, many=True)
    password = serializers.CharField(required=False, allow_blank=True, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'nickname', 'first_name', 'last_name', 'password', 'social_id_number', 'personal_id_number', 'mobile_phone_number', 'phone_number', 'education_level', 'admin', 'crud_project', 'projects', 'subOrganizations', 'create_date']
    