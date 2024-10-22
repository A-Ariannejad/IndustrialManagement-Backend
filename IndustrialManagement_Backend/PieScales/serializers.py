from rest_framework import serializers
from .models import PieScale
from IndustrialManagement_Backend.serializers import GetProjectSerializer

class GetPieScaleWithoutProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieScale
        fields = '__all__'

class CreatePieScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieScale
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['project'] = GetProjectSerializer(instance.project, context={'request': self.context['request'], 'sub_org': instance.project.subOrganization}).data
        return ret