from rest_framework.permissions import BasePermission
from CustomUsers.models import LogicUser
from rest_framework import generics, viewsets, status
from .serializers import PermissionSerializer
from .models import CustomUserPermission
from IndustrialManagement_Backend.serializers import CustomValidation

class IsController(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.user_permissions.is_controller:
                return True
        return False

class IsViewer(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.user_permissions.is_viewer:
                return True
        return False
    
class IsCalculator(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.user_permissions.is_calculator:
                return True
        return False
    
class IsSupporter(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.user_permissions.is_supporter:
                return True
        return False
    
class IsLogin(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user is not None:
            return True
        return False

class PermissionShowView(generics.RetrieveAPIView):
    queryset = CustomUserPermission.objects.all()
    serializer_class = PermissionSerializer
    # permission_classes = [IsEditUser]
    lookup_field = 'id'

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = CustomUserPermission.objects.all()
    serializer_class = PermissionSerializer
    # permission_classes = [IsEditUser]

class PermissionCreateView(generics.CreateAPIView):
    queryset = CustomUserPermission.objects.all()
    serializer_class = PermissionSerializer
    # permission_classes = [IsEditUser]

    def perform_create(self, serializer):
        instance = serializer.instance
        if instance.name == 'User':
            raise CustomValidation("User is reserved", "", status_code=status.HTTP_400_BAD_REQUEST)
        if instance.name == 'SuperAdmin':
            raise CustomValidation("SuperAdmin is reserved", "", status_code=status.HTTP_400_BAD_REQUEST)
        if serializer.validated_data['name'] == 'User':
            raise CustomValidation("User is reserved", "", status_code=status.HTTP_400_BAD_REQUEST)
        if serializer.validated_data['name'] == 'SuperAdmin':
            raise CustomValidation("SuperAdmin is reserved", "", status_code=status.HTTP_400_BAD_REQUEST)
        return super().perform_create(serializer)

class PermissionUpdateView(generics.UpdateAPIView):
    queryset = CustomUserPermission.objects.all()
    serializer_class = PermissionSerializer
    # permission_classes = [IsEditUser]

    def perform_update(self, serializer):
        instance = serializer.instance
        if instance.name == 'User':
            raise CustomValidation("User is reserved", "", status_code=status.HTTP_400_BAD_REQUEST)
        if instance.name == 'SuperAdmin':
            raise CustomValidation("SuperAdmin is reserved", "", status_code=status.HTTP_400_BAD_REQUEST)
        if serializer.validated_data['name'] == 'User':
            raise CustomValidation("User is reserved", "", status_code=status.HTTP_400_BAD_REQUEST)
        if serializer.validated_data['name'] == 'SuperAdmin':
            raise CustomValidation("SuperAdmin is reserved", "", status_code=status.HTTP_400_BAD_REQUEST)
        return super().perform_update(serializer)

class PermissionDeleteView(generics.DestroyAPIView):
    queryset = CustomUserPermission.objects.all()
    serializer_class = PermissionSerializer
    # permission_classes = [IsEditUser]

    def perform_destroy(self, instance):
        if instance.name == 'User':
            raise CustomValidation("User can not be deleted", "", status_code=status.HTTP_400_BAD_REQUEST)
        if instance.name == 'SuperAdmin':
            raise CustomValidation("SuperAdmin can not be deleted", "", status_code=status.HTTP_400_BAD_REQUEST)
        return super().perform_destroy(instance)

