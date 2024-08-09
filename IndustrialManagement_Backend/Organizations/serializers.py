from rest_framework import serializers
from .models import Organization
from IndustrialManagement_Backend.serializers import GetCustomUserSerializer

class CreateOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['owner'] = GetCustomUserSerializer(instance.owner).data
        return ret