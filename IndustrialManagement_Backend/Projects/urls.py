from django.urls import path
from .views import ProjectCreateView, ProjectViewSet, ProjectUpdateView, ProjectShowView, ProjectDeleteView

urlpatterns = [
    path('show/<int:id>/', ProjectShowView.as_view(), name='show'),
    path('list/', ProjectViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProjectUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='delete'),
]