from .serializers import CreateTimeScaleSerializer, GetTimeScaleWithoutProjectSerializer
from IndustrialManagement_Backend.serializers import GetTimeScaleSerializer
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

class TimeScaleShowByProjectViewSet(viewsets.ModelViewSet):
    serializer_class = GetTimeScaleWithoutProjectSerializer
    # permission_classes = [IsUserAccess]

    def get_queryset(self):
        queryset = TimeScale.objects.filter(project=self.kwargs['pk']).all().order_by('-create_date')
        return queryset

class TimeScaleCreateView(generics.CreateAPIView):
    queryset = TimeScale.objects.all()
    serializer_class = CreateTimeScaleSerializer
    # permission_classes = [IsUserAccess]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class TimeScaleUpdateView(generics.UpdateAPIView):
    queryset = TimeScale.objects.all()
    serializer_class = CreateTimeScaleSerializer
    # permission_classes = [IsUserAccess]
    
class TimeScaleDeleteView(generics.DestroyAPIView):
    queryset = TimeScale.objects.all()
    serializer_class = GetTimeScaleSerializer
    # permission_classes = [IsUserAccess]
    