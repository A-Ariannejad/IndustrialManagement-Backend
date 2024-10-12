from .serializers import GetCustomUserProfileSerializer, CreateCustomUserSerializer, UpdateCustomUserSerializer
from IndustrialManagement_Backend.serializers import GetCustomUserSerializer
from CustomUserPermissions.views import IsUserAccess
from .models import CustomUser, CustomUserPermission
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import generics, permissions, viewsets, status

class MyCustomUserShowView(generics.RetrieveAPIView):
    serializer_class = GetCustomUserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
            user = CustomUser.objects.filter(id=request.user.id).first()
            if not user:
                return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

class CustomUserShowView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = GetCustomUserSerializer
    # permission_classes = [IsUserAccess]
    lookup_field = 'id'

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-create_date')
    serializer_class = GetCustomUserSerializer
    # permission_classes = [IsUserAccess]

class CustomUserAdminViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-create_date')
    serializer_class = GetCustomUserProfileSerializer
    # permission_classes = [IsUserAccess]

class CreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateCustomUserSerializer
    # permission_classes = [IsUserAccess]
      
    def perform_create(self, serializer):
        serializer.save(password=make_password(self.request.data.get('password')))

class CustomUserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateCustomUserSerializer
    # permission_classes = [IsUserAccess]
    def perform_update(self, serializer):
        new_username = self.request.data.get('username')
        new_nickname = self.request.data.get('nickname')
        new_education_level = self.request.data.get('education_level')
        new_user_permissions = self.request.data.get('user_permissions')
        new_password = self.request.data.get('password')
        user = CustomUser.objects.filter(id=self.kwargs['pk']).first()
        serializer.user_permissions = user.user_permissions
        if not new_username: 
            new_username = user.username
        if not new_nickname: 
            new_nickname = user.nickname
        if not new_education_level: 
            new_education_level = user.education_level
        if not new_user_permissions: 
            new_user_permissions = user.user_permissions
        else:
            permission = CustomUserPermission.objects.filter(id=new_user_permissions).first()
            if permission:
                serializer.user_permissions = permission
            else:
                new_user_permissions = user.user_permissions
        if new_password:
            new_password=make_password(self.request.data.get('password'))
        else:
            new_password=user.password
        serializer.save(username=new_username, nickname=new_nickname, education_level=new_education_level, user_permissions=new_user_permissions, password=new_password)
    
class CustomUserDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = GetCustomUserProfileSerializer
    # permission_classes = [IsUserAccess]
    