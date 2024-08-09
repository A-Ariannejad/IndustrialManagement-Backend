from .serializers import CreateProjectSerializer
from IndustrialManagement_Backend.serializers import GetProjectSerializer
from CustomUserPermissions.views import IsUserAccess
from .models import Project
from rest_framework import generics, viewsets

class ProjectShowView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = GetProjectSerializer
    # permission_classes = [IsUserAccess]
    lookup_field = 'id'

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-create_date')
    serializer_class = GetProjectSerializer
    # permission_classes = [IsUserAccess]

class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = CreateProjectSerializer
    # permission_classes = [IsUserAccess]

class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = CreateProjectSerializer
    # permission_classes = [IsUserAccess]
    
class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = GetProjectSerializer
    # permission_classes = [IsUserAccess]
    