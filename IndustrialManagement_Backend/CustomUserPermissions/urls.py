from django.urls import path
from .views import PermissionCreateView, PermissionDeleteView, PermissionShowView, PermissionUpdateView, PermissionViewSet

urlpatterns = [
    path('show/<int:id>/', PermissionShowView.as_view(), name='show'),
    path('list/', PermissionViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', PermissionCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PermissionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PermissionDeleteView.as_view(), name='delete'),
]