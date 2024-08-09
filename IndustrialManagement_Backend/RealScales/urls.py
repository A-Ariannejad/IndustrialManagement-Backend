from django.urls import path
from .views import RealScaleCreateView, RealScaleViewSet, RealScaleUpdateView, RealScaleShowView, RealScaleDeleteView

urlpatterns = [
    path('show/<int:id>/', RealScaleShowView.as_view(), name='show'),
    path('list/', RealScaleViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', RealScaleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', RealScaleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', RealScaleDeleteView.as_view(), name='delete'),
]