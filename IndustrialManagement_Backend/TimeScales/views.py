from .serializers import CreateTimeScaleSerializer
from IndustrialManagement_Backend.serializers import GetTimeScaleSerializer
from CustomUserPermissions.views import IsUserAccess
from .models import TimeScale
from rest_framework import generics, viewsets

class TimeScaleShowView(generics.RetrieveAPIView):
    queryset = TimeScale.objects.all()
    serializer_class = GetTimeScaleSerializer
    # permission_classes = [IsUserAccess]
    lookup_field = 'id'

class TimeScaleViewSet(viewsets.ModelViewSet):
    queryset = TimeScale.objects.all().order_by('-create_date')
    serializer_class = GetTimeScaleSerializer
    # permission_classes = [IsUserAccess]

class TimeScaleCreateView(generics.CreateAPIView):
    queryset = TimeScale.objects.all()
    serializer_class = CreateTimeScaleSerializer
    # permission_classes = [IsUserAccess]

class TimeScaleUpdateView(generics.UpdateAPIView):
    queryset = TimeScale.objects.all()
    serializer_class = CreateTimeScaleSerializer
    # permission_classes = [IsUserAccess]
    
class TimeScaleDeleteView(generics.DestroyAPIView):
    queryset = TimeScale.objects.all()
    serializer_class = GetTimeScaleSerializer
    # permission_classes = [IsUserAccess]
    