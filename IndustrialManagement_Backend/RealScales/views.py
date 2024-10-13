from .serializers import CreateRealScaleSerializer, GetRealScaleWithoutProjectSerializer
from IndustrialManagement_Backend.serializers import GetRealScaleSerializer
from CustomUserPermissions.views import IsUserAccess
from .models import RealScale
from rest_framework import generics, viewsets

class RealScaleShowView(generics.RetrieveAPIView):
    queryset = RealScale.objects.all()
    serializer_class = GetRealScaleSerializer
    # permission_classes = [IsUserAccess]
    lookup_field = 'id'

class RealScaleViewSet(viewsets.ModelViewSet):
    queryset = RealScale.objects.all().order_by('-create_date')
    serializer_class = GetRealScaleSerializer
    # permission_classes = [IsUserAccess]

class RealScaleShowByProjectViewSet(viewsets.ModelViewSet):
    serializer_class = GetRealScaleWithoutProjectSerializer
    # permission_classes = [IsUserAccess]

    def get_queryset(self):
        queryset = RealScale.objects.filter(project=self.kwargs['pk']).all().order_by('-create_date')
        return queryset

class RealScaleCreateView(generics.CreateAPIView):
    queryset = RealScale.objects.all()
    serializer_class = CreateRealScaleSerializer
    # permission_classes = [IsUserAccess]

class RealScaleUpdateView(generics.UpdateAPIView):
    queryset = RealScale.objects.all()
    serializer_class = CreateRealScaleSerializer
    # permission_classes = [IsUserAccess]
    
class RealScaleDeleteView(generics.DestroyAPIView):
    queryset = RealScale.objects.all()
    serializer_class = GetRealScaleSerializer
    # permission_classes = [IsUserAccess]
    