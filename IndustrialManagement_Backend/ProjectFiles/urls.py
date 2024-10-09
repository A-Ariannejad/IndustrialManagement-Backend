from django.urls import path
from .views import ProjectFileCreateView, ProjectFileViewSet, ProjectFileUpdateView, ProjectFileShowView, ProjectFileDeleteView

urlpatterns = [
    path('show/<int:id>/', ProjectFileShowView.as_view(), name='show'),
    path('list/', ProjectFileViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', ProjectFileCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProjectFileUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProjectFileDeleteView.as_view(), name='delete'),
]