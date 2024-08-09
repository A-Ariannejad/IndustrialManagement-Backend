from rest_framework import status
from rest_framework import serializers
from rest_framework.exceptions import APIException
from CustomUserPermissions.models import CustomUserPermission
from CustomUsers.models import CustomUser
from Organizations.models import Organization
from SubOrganizations.models import SubOrganization
from Projects.models import Project
from RealScales.models import RealScale

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

class GetSubOrganizationSerializer(serializers.ModelSerializer):
    owner = GetCustomUserSerializer()
    organization = GetOrganizationSerializer()
    class Meta:
        model = SubOrganization
        fields = '__all__'

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