from .serializers import GetCustomUserProfileSerializer, GetCustomUserSerializer, CreateCustomUserSerializer
from CustomUserPermissions.views import IsAddSubOrganization, IsAddManager, IsAddProject, IsView
from CustomUserPermissions.models import CustomUserPermission
from IndustrialManagement_Backend.serializers import CustomValidation
from .models import CustomUser, LogicUser
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import generics, permissions, viewsets, status
import jwt

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
    # permission_classes = [IsEditUser]
    lookup_field = 'id'

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-create_date')
    serializer_class = GetCustomUserSerializer
    # permission_classes = [IsEditUser]

class CreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateCustomUserSerializer
    permission_classes = [permissions.AllowAny]
      
    def perform_create(self, serializer):
        serializer.save(password=make_password(self.request.data.get('password')))

class CustomUserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateCustomUserSerializer
    # permission_classes = [IsEditUser]

    def perform_update(self, serializer):
        serializer.save(password=make_password(self.request.data.get('password')))
    
class CustomUserDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = GetCustomUserProfileSerializer
    # permission_classes = [IsEditUser]
    