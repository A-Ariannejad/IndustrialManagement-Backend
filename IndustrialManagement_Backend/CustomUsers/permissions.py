from rest_framework.permissions import BasePermission
from CustomUsers.models import LogicUser
from rest_framework import status
from IndustrialManagement_Backend.serializers import CustomValidation

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.admin:
                return True
        raise CustomValidation("شما اجازه این کار را ندارید", "", status_code=status.HTTP_403_FORBIDDEN)
    
class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.is_superuser:
                return True
        raise CustomValidation("شما اجازه این کار را ندارید", "", status_code=status.HTTP_403_FORBIDDEN)
