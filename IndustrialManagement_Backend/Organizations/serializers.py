from rest_framework import serializers
from .models import Organization
from CustomUsers.serializers import GetCustomUserSerializer

class GetOrganizationSerializer(serializers.ModelSerializer):
    boss = GetCustomUserSerializer()
    class Meta:
        model = Organization
        fields = '__all__'

class CreateOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['boss'] = GetCustomUserSerializer(instance.boss).data
        return ret