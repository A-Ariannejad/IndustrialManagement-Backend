from rest_framework import status
from rest_framework import serializers
from rest_framework.exceptions import APIException
from CustomUserPermissions.models import CustomUserPermission
from CustomUsers.models import CustomUser
from Organizations.models import Organization
from SubOrganizations.models import SubOrganization
from Projects.models import Project
from RealScales.models import RealScale
from TimeScales.models import TimeScale
from PieScales.models import PieScale
from ProjectFiles.models import ProjectFile

class CustomValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, field, status_code):
        if status_code is not None:self.status_code = status_code
        if detail is not None:
            self.detail = detail
        else: self.detail = self.default_detail

class GetPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserPermission
        fields = ['id', 'name', 'add_subOrganization', 'add_manager', 'add_project', 'user_access']

class GetCustomUserSerializer(serializers.ModelSerializer):
    user_permissions = GetPermissionSerializer()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'user_permissions']

class GetOrganizationSerializer(serializers.ModelSerializer):
    owner = GetCustomUserSerializer()
    class Meta:
        model = Organization
        fields = '__all__'

class GetCustomUser_ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class GetSubOrganization_CustomUserSerializer(serializers.ModelSerializer):
    user_permissions = GetPermissionSerializer()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'user_permissions', 'education_level', 'mobile_phone_number']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['projects'] = GetCustomUser_ProjectSerializer(instance.project_set.all(), many=True).data
        return ret


class GetSubOrganizationSerializer(serializers.ModelSerializer):
    owner = GetCustomUserSerializer()
    organization = GetOrganizationSerializer()
    
    class Meta:
        model = SubOrganization
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        users = instance.customuser_set.all()
        ret['people'] = GetSubOrganization_CustomUserSerializer(users, many=True).data
        ret['owner'] = GetCustomUserSerializer(instance.owner).data
        ret['organization'] = GetOrganizationSerializer(instance.organization).data
        return ret
    
class GetSelectSubOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubOrganization
        fields = ['id', 'nickname']

class GetProjectSerializer(serializers.ModelSerializer):
    owner = GetCustomUserSerializer()
    subOrganization = GetSubOrganizationSerializer()
    class Meta:
        model = Project
        fields = '__all__'

class GetRealScaleSerializer(serializers.ModelSerializer):
    project = GetProjectSerializer()
    class Meta:
        model = RealScale
        fields = '__all__'

class GetTimeScaleSerializer(serializers.ModelSerializer):
    project = GetProjectSerializer()
    class Meta:
        model = TimeScale
        fields = '__all__'

class GetPieScaleSerializer(serializers.ModelSerializer):
    project = GetProjectSerializer()
    class Meta:
        model = PieScale
        fields = '__all__'

class GetProjectFileSerializer(serializers.ModelSerializer):
    uploader = GetCustomUserSerializer()
    project = GetProjectSerializer()
    class Meta:
        model = ProjectFile
        fields = '__all__'