from django.urls import path
from .views import OrganizationCreateView, OrganizationViewSet, OrganizationUpdateView, OrganizationShowView, OrganizationDeleteView

urlpatterns = [
    path('show/<int:id>/', OrganizationShowView.as_view(), name='show'),
    path('list/', OrganizationViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', OrganizationCreateView.as_view(), name='create'),
    path('update/<int:pk>/', OrganizationUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', OrganizationDeleteView.as_view(), name='delete'),
]