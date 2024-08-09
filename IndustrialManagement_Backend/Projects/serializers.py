from rest_framework import serializers
from .models import Project
from SubOrganizations.serializers import GetSubOrganizationSerializer, GetCustomUserSerializer

class GetProjectSerializer(serializers.ModelSerializer):
    owner = GetCustomUserSerializer()
    subOrganization = GetSubOrganizationSerializer()
    class Meta:
        model = Project
        fields = '__all__'

class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['owner'] = GetCustomUserSerializer(instance.owner).data
        ret['subOrganization'] = GetSubOrganizationSerializer(instance.subOrganization).data
        return ret