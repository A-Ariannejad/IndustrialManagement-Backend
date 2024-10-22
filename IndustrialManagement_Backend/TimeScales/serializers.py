from rest_framework import serializers
from .models import TimeScale
from IndustrialManagement_Backend.serializers import GetProjectSerializer

class GetTimeScaleWithoutProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeScale
        fields = '__all__'

class CreateTimeScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeScale
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['project'] = GetProjectSerializer(instance.project, context={'request': self.context['request'], 'sub_org': instance.project.subOrganization}).data
        return ret