from django.urls import path
from .views import TimeScaleCreateView, TimeScaleViewSet, TimeScaleUpdateView, TimeScaleShowView, TimeScaleDeleteView, TimeScaleShowByProjectViewSet

urlpatterns = [
    path('show/<int:id>/', TimeScaleShowView.as_view(), name='show'),
    path('showbyprojec/<int:pk>/', TimeScaleShowByProjectViewSet.as_view({'get': 'list'}), name='showbyprojec'),
    path('list/', TimeScaleViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', TimeScaleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TimeScaleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TimeScaleDeleteView.as_view(), name='delete'),
]