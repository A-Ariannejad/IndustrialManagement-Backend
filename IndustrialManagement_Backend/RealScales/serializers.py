from rest_framework import serializers
from .models import RealScale
from IndustrialManagement_Backend.serializers import GetProjectSerializer

class CreateRealScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealScale
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['project'] = GetProjectSerializer(instance.project).data
        return ret