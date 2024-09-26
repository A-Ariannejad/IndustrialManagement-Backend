from rest_framework.permissions import BasePermission
from CustomUsers.models import LogicUser, CustomUser
from rest_framework import generics, viewsets, status
from IndustrialManagement_Backend.serializers import GetPermissionSerializer
from .models import CustomUserPermission
from IndustrialManagement_Backend.serializers import CustomValidation

class IsAddSubOrganization(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.user_permissions.add_subOrganization:
                return True
        return False

class IsAddManager(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.user_permissions.add_manager:
                return True
        return False
    
class IsAddProject(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.user_permissions.add_project:
                return True
        return False
    
    
class IsUserAccess(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.user_permissions.user_access:
                return True
        return False
    
class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.user_permissions.name == 'SuperAdmin':
                return True
        return False

class PermissionShowView(generics.RetrieveAPIView):
    queryset = CustomUserPermission.objects.all()
    serializer_class = GetPermissionSerializer
    permission_classes = [IsSuperAdmin]
    lookup_field = 'id'

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = CustomUserPermission.objects.all()
    serializer_class = GetPermissionSerializer
    permission_classes = [IsSuperAdmin]

class PermissionCreateView(generics.CreateAPIView):
    queryset = CustomUserPermission.objects.all()
    serializer_class = GetPermissionSerializer
    permission_classes = [IsSuperAdmin]

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        if validated_data.get('name') == 'User':
            raise CustomValidation("User is reserved", "", status_code=status.HTTP_400_BAD_REQUEST)
        if validated_data.get('name') == 'SuperAdmin':
            raise CustomValidation("SuperAdmin is reserved", "", status_code=status.HTTP_400_BAD_REQUEST)
        return super().perform_create(serializer)

class PermissionUpdateView(generics.UpdateAPIView):
    queryset = CustomUserPermission.objects.all()
    serializer_class = GetPermissionSerializer
    permission_classes = [IsSuperAdmin]

    def perform_update(self, serializer):
        validated_data = serializer.validated_data
        if validated_data.get('name') == 'User':
            raise CustomValidation("User is reserved", "", status_code=status.HTTP_400_BAD_REQUEST)
        if validated_data.get('name') == 'SuperAdmin':
            raise CustomValidation("SuperAdmin is reserved", "", status_code=status.HTTP_400_BAD_REQUEST)
        return super().perform_update(serializer)

class PermissionDeleteView(generics.DestroyAPIView):
    queryset = CustomUserPermission.objects.all()
    serializer_class = GetPermissionSerializer
    permission_classes = [IsSuperAdmin]

    def perform_destroy(self, instance):
        if instance.name == 'User':
            raise CustomValidation("User can not be deleted", "", status_code=status.HTTP_400_BAD_REQUEST)
        if instance.name == 'SuperAdmin':
            raise CustomValidation("SuperAdmin can not be deleted", "", status_code=status.HTTP_400_BAD_REQUEST)
        permission = CustomUserPermission.objects.filter(name='User').first()
        CustomUser.objects.filter(user_permissions__name=instance.name).all().update(user_permissions=permission)
        return super().perform_destroy(instance)


