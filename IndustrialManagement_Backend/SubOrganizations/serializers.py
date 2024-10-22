from rest_framework import serializers
from .models import SubOrganization
from IndustrialManagement_Backend.serializers import GetOrganizationSerializer, GetCustomUserSerializer

class CreateSubOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubOrganization
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['owner'] = GetCustomUserSerializer(instance.owner).data
        ret['organization'] = GetOrganizationSerializer(instance.organization, context={'request': self.context['request']}).data
        return ret