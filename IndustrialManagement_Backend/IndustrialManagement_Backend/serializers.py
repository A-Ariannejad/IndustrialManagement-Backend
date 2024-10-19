from rest_framework import status
from rest_framework import serializers
from rest_framework.exceptions import APIException
from CustomUsers.models import CustomUser
from Organizations.models import Organization
from SubOrganizations.models import SubOrganization
from Projects.models import Project
from RealScales.models import RealScale
from TimeScales.models import TimeScale
from PieScales.models import PieScale
from ProjectFiles.models import ProjectFile
from django.db.models import Q

def scale_type_queryset(self):
    user = self.request.user
    if user.admin:
        return self.queryset
    user_projects = Project.objects.filter(Q(owner=user) | Q(id__in=user.projects.all()))
    return self.queryset.filter(project__in=user_projects)

class CustomValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, field, status_code):
        if status_code is not None:self.status_code = status_code
        if detail is not None:
            self.detail = detail
        else: self.detail = self.default_detail

class GetCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'admin', 'crud_project', 'is_superuser', 'projects']

class GetOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

    def get_sub_organs(self, instance):
        request_user = self.context['request'].user
        sub_organizations = instance.suborganization_set.all()
        if not request_user.admin:
            sub_organizations = sub_organizations.filter(
                Q(owner=request_user) |
                Q(project__owner=request_user) |
                Q(project__in=request_user.projects.all())
            ).distinct()
        return GetSubOrganizationSerializer(sub_organizations, many=True, context={'request': self.context['request']}).data

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['sub_organs'] = self.get_sub_organs(instance)
        return ret
    
class GetCustomUser_ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class GetSubOrganization_CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'education_level', 'mobile_phone_number']

    def to_representation(self, instance):
        request_user = self.context['request'].user
        sub_org = self.context['sub_org']
        ret = super().to_representation(instance)
        if request_user.admin or instance == request_user:
            ret['projects'] = GetCustomUser_ProjectSerializer(instance.project_set.filter(subOrganization=sub_org), many=True).data
        else:
            filtered_projects = instance.project_set.filter(Q(subOrganization=sub_org) & (Q(owner=request_user) | Q(id__in=request_user.projects.all())))
            ret['projects'] = GetCustomUser_ProjectSerializer(filtered_projects, many=True).data
        return ret

class GetSubOrganizationSerializer(serializers.ModelSerializer):
    owner = GetCustomUserSerializer()
    
    class Meta:
        model = SubOrganization
        fields = '__all__'
    
    def to_representation(self, instance):
        request_user = self.context['request'].user
        ret = super().to_representation(instance)
        users = instance.customuser_set.all()
        if request_user.admin or instance.owner == request_user:
            ret['people'] = GetSubOrganization_CustomUserSerializer(users, many=True, context={'request': self.context['request'], 'sub_org': instance}).data
        else:
            filtered_users = users.filter(Q(id=request_user.id) | Q(project__subOrganization=instance, project__id__in=request_user.projects.all())).distinct()
            ret['people'] = GetSubOrganization_CustomUserSerializer(filtered_users, many=True, context={'request': self.context['request'], 'sub_org': instance}).data
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