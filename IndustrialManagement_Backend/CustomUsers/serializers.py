from rest_framework import serializers
from .models import CustomUser
from CustomUserPermissions.serializers import PermissionSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.exceptions import ValidationError


class GetCustomUserSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'user_permissions']

class GetCustomUserProfileSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'create_date', 'user_permissions']

class CreateCustomUserSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','username','email', 'password', 'first_name', 'last_name', 'create_date', 'user_permissions']
    
class UpdateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
    
    def update(self, instance, validated_data):
        user = CustomUser.objects.get(id=self.context['token_id'])
        if user.id == self.context['user_id']:
            return super().update(instance, validated_data)
        else:
            raise ValidationError("not your account")

class UpdatePermissionCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'user_permissions']
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['user_permissions'] = PermissionSerializer(instance.user_permissions).data
        return ret
    
class LoginCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password',]

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['password']

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

class SetPasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField()