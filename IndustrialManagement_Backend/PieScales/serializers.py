from rest_framework import serializers
from .models import PieScale
from IndustrialManagement_Backend.serializers import GetProjectSerializer

class CreatePieScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieScale
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['project'] = GetProjectSerializer(instance.project).data
        return ret