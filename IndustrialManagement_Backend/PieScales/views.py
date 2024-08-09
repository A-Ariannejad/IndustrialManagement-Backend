from .serializers import CreatePieScaleSerializer
from IndustrialManagement_Backend.serializers import GetPieScaleSerializer
from CustomUserPermissions.views import IsUserAccess
from .models import PieScale
from rest_framework import generics, viewsets

class PieScaleShowView(generics.RetrieveAPIView):
    queryset = PieScale.objects.all()
    serializer_class = GetPieScaleSerializer
    # permission_classes = [IsUserAccess]
    lookup_field = 'id'

class PieScaleViewSet(viewsets.ModelViewSet):
    queryset = PieScale.objects.all().order_by('-create_date')
    serializer_class = GetPieScaleSerializer
    # permission_classes = [IsUserAccess]

class PieScaleCreateView(generics.CreateAPIView):
    queryset = PieScale.objects.all()
    serializer_class = CreatePieScaleSerializer
    # permission_classes = [IsUserAccess]

class PieScaleUpdateView(generics.UpdateAPIView):
    queryset = PieScale.objects.all()
    serializer_class = CreatePieScaleSerializer
    # permission_classes = [IsUserAccess]
    
class PieScaleDeleteView(generics.DestroyAPIView):
    queryset = PieScale.objects.all()
    serializer_class = GetPieScaleSerializer
    # permission_classes = [IsUserAccess]
    