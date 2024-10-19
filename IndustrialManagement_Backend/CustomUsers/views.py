from .serializers import GetCustomUserProfileSerializer, CreateCustomUserSerializer, UpdateCustomUserSerializer
from IndustrialManagement_Backend.serializers import GetCustomUserSerializer, Organization, SubOrganization, Project, CustomValidation
from .models import CustomUser
from .permissions import IsSuperAdmin
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
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-create_date')
    serializer_class = GetCustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomUserAdminViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-create_date')
    serializer_class = GetCustomUserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

class CreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateCustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
      
    def perform_create(self, serializer):
        serializer.save(password=make_password(self.request.data.get('password')))

class CustomUserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateCustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    
    def perform_update(self, serializer):
        new_username = self.request.data.get('username')
        new_nickname = self.request.data.get('nickname')
        new_education_level = self.request.data.get('education_level')
        new_password = self.request.data.get('password')
        user = CustomUser.objects.filter(id=self.kwargs['pk']).first()
        if not new_username: 
            new_username = user.username
        if not new_nickname: 
            new_nickname = user.nickname
        if not new_education_level: 
            new_education_level = user.education_level
        if new_password:
            new_password=make_password(self.request.data.get('password'))
        else:
            new_password=user.password
        serializer.save(username=new_username, nickname=new_nickname, education_level=new_education_level, password=new_password)
    
class CustomUserDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = GetCustomUserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    
    def perform_destroy(self, instance):
        user_id = self.kwargs['pk']
        user = CustomUser.objects.filter(id=user_id).first()
        organizations = Organization.objects.filter(owner=user).first()
        subOrganizations = SubOrganization.objects.filter(owner=user).first()
        projects = Project.objects.filter(owner=user).first()
        if organizations or subOrganizations or projects:
            raise CustomValidation("کاربر صاحب سازمان یا مرکز یا پروژه قابل پاک کردن نیست", "", status_code=status.HTTP_400_BAD_REQUEST)
        return super().perform_destroy(instance)
    