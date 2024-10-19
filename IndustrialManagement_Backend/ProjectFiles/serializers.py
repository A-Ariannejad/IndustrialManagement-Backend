from rest_framework import serializers
from .models import ProjectFile
from IndustrialManagement_Backend.serializers import GetProjectSerializer, GetCustomUserSerializer

class GetProjectFileWithoutProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = '__all__'

class CreateProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ['name', 'file', 'project', 'description', 'create_date']
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['uploader'] = GetCustomUserSerializer(instance.uploader).data
        ret['project'] = GetProjectSerializer(instance.project).data
        return ret