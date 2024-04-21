from django.urls import path
from .views import CreateView, LoginView, CustomUserViewSet, CustomUserUpdateView, CustomUserShowView, CustomUserDeleteView, MyCustomUserShowView, ForgetSendPasswordResetView, ForgetGetPasswordResetView
from .views import CustomUserChangePasswordView, CustomUserUpdatePermissionView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('myshow/', MyCustomUserShowView.as_view(), name='myshow'),
    path('show/<int:id>/', CustomUserShowView.as_view(), name='show'),
    path('list/', CustomUserViewSet.as_view({'get': 'list'}), name='list'),
    path('signup/', CreateView.as_view(), name='create'),
    path('updatepermission/<int:pk>/', CustomUserUpdatePermissionView.as_view(), name='updatepermission'),
    path('forgetsendpassword/', ForgetSendPasswordResetView.as_view(), name='forgetpassword'),
    path('forgetgetpassword/<uidb64>/<token>/', ForgetGetPasswordResetView.as_view(),name='forgetgetpassword'),
    path('update/<int:pk>/', CustomUserUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CustomUserDeleteView.as_view(), name='delete'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('changepassword/', CustomUserChangePasswordView.as_view(), name='change_password'),
]