from rest_framework import serializers
from .models import TimeScale
from IndustrialManagement_Backend.serializers import GetProjectSerializer

class CreateTimeScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeScale
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['project'] = GetProjectSerializer(instance.project).data
        return ret