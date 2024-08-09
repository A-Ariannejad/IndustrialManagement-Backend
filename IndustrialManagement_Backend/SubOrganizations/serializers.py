from rest_framework import serializers
from .models import SubOrganization
from Organizations.serializers import GetOrganizationSerializer, GetCustomUserSerializer

class GetSubOrganizationSerializer(serializers.ModelSerializer):
    owner = GetCustomUserSerializer()
    organization = GetOrganizationSerializer()
    class Meta:
        model = SubOrganization
        fields = '__all__'

class CreateSubOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubOrganization
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['owner'] = GetCustomUserSerializer(instance.owner).data
        ret['organization'] = GetOrganizationSerializer(instance.organization).data
        return ret