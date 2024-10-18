from .serializers import CreatePieScaleSerializer, GetPieScaleWithoutProjectSerializer
from IndustrialManagement_Backend.serializers import GetPieScaleSerializer
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

class PieScaleShowByProjectViewSet(viewsets.ModelViewSet):
    serializer_class = GetPieScaleWithoutProjectSerializer
    # permission_classes = [IsUserAccess]

    def get_queryset(self):
        queryset = PieScale.objects.filter(project=self.kwargs['pk']).all().order_by('-create_date')
        return queryset

class PieScaleCreateView(generics.CreateAPIView):
    queryset = PieScale.objects.all()
    serializer_class = CreatePieScaleSerializer
    # permission_classes = [IsUserAccess]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class PieScaleUpdateView(generics.UpdateAPIView):
    queryset = PieScale.objects.all()
    serializer_class = CreatePieScaleSerializer
    # permission_classes = [IsUserAccess]
    
class PieScaleDeleteView(generics.DestroyAPIView):
    queryset = PieScale.objects.all()
    serializer_class = GetPieScaleSerializer
    # permission_classes = [IsUserAccess]
    