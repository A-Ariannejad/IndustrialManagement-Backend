from django.urls import path
from .views import PieScaleCreateView, PieScaleViewSet, PieScaleUpdateView, PieScaleShowView, PieScaleDeleteView

urlpatterns = [
    path('show/<int:id>/', PieScaleShowView.as_view(), name='show'),
    path('list/', PieScaleViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', PieScaleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PieScaleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PieScaleDeleteView.as_view(), name='delete'),
]