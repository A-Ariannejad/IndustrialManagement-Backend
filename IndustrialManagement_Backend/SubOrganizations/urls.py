from django.urls import path
from .views import SubOrganizationCreateView, SubOrganizationViewSet, SubOrganizationUpdateView, SubOrganizationShowView, SubOrganizationDeleteView

urlpatterns = [
    path('show/<int:id>/', SubOrganizationShowView.as_view(), name='show'),
    path('list/', SubOrganizationViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', SubOrganizationCreateView.as_view(), name='create'),
    path('update/<int:pk>/', SubOrganizationUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', SubOrganizationDeleteView.as_view(), name='delete'),
]