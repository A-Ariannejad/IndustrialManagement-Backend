from .serializers import GetCustomUserProfileSerializer, GetCustomUserSerializer, CreateCustomUserSerializer
from CustomUserPermissions.views import IsAddSubOrganization, IsAddManager, IsAddProject, IsUserAccess
from CustomUserPermissions.models import CustomUserPermission
from IndustrialManagement_Backend.serializers import CustomValidation
from .models import CustomUser, LogicUser
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets, status, views
import jwt
from django.core.mail import send_mail

def send_reset_password_email(email, website, uidb64, token):
    reset_url = f"localhost:3000/auth/newpassword/{uidb64}/{token}/"
    subject = 'Password Reset'
    message = f"Please click the following link to reset your password:\n {reset_url} "
    send_mail(subject, message, 'myemail@gmail.com', [email])


class MyCustomUserShowView(generics.RetrieveAPIView):
    serializer_class = GetCustomUserProfileSerializer
    # permission_classes = [IsLogin]
    
    def get(self, request, *args, **kwargs):
        try:
            user_id = request.user.id
            user = CustomUser.objects.get(id=user_id)
            serializer = self.serializer_class(user)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

class CustomUserShowView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = GetCustomUserSerializer
    permission_classes = [IsUserAccess]
    lookup_field = 'id'

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-create_date')
    serializer_class = GetCustomUserSerializer
    permission_classes = [IsUserAccess]

class CreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateCustomUserSerializer
    permission_classes = [IsUserAccess]
      
    def perform_create(self, serializer):
        permission = CustomUserPermission.objects.filter(name='User', is_controller=False, is_viewer=False, is_calculator=False, is_supporter=False).first()
        if not permission:
            permission = CustomUserPermission.objects.create(name='User', is_controller=False, is_viewer=False, is_calculator=False, is_supporter=False)
        serializer.save(password=make_password(self.request.data.get('password')), user_permissions=permission)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginCustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('phone_number') 
        password = request.data.get('password') 
        user = CustomUser.objects.filter(email = email).first()
        
        if user and check_password(password, user.password):
            encoded_jwt = jwt.encode({"email": user.email}, "56s4fs8df4d8af4198h489r4hdy85k4du8l94k8g581d8f", algorithm="HS256")
            response = Response("Login Successful", status=status.HTTP_200_OK)
            response.set_cookie('Token', encoded_jwt)
            return response
        else:
            return Response("Login Failed", status=status.HTTP_401_UNAUTHORIZED)

class CustomUserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateCustomUserSerializer
    permission_classes = [IsUserAccess]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['token_id'] = self.request.user.id
        context['user_id'] = self.kwargs['pk'] 
        return context
    
class CustomUserUpdatePermissionView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UpdatePermissionCustomUserSerializer
    # permission_classes = [IsEditUser]
    
class CustomUserDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = GetCustomUserProfileSerializer
    permission_classes = [IsUserAccess]
    
class CustomUserChangePasswordView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ChangePasswordSerializer
    # permission_classes = [IsEditUser]
    