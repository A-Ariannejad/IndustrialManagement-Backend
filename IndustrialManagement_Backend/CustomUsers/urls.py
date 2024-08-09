from django.urls import path
from .views import CreateView, CustomUserViewSet, CustomUserUpdateView, CustomUserShowView, CustomUserDeleteView, MyCustomUserShowView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('myshow/', MyCustomUserShowView.as_view(), name='myshow'),
    path('show/<int:id>/', CustomUserShowView.as_view(), name='show'),
    path('list/', CustomUserViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', CreateView.as_view(), name='create'),
    path('update/<int:pk>/', CustomUserUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CustomUserDeleteView.as_view(), name='delete'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]