from .serializers import CreateProjectFileSerializer
from IndustrialManagement_Backend.serializers import GetProjectFileSerializer
from CustomUserPermissions.views import IsUserAccess
from .models import ProjectFile
from rest_framework import generics, viewsets

class ProjectFileShowView(generics.RetrieveAPIView):
    queryset = ProjectFile.objects.all()
    serializer_class = GetProjectFileSerializer
    # permission_classes = [IsUserAccess]
    lookup_field = 'id'

class ProjectFileViewSet(viewsets.ModelViewSet):
    queryset = ProjectFile.objects.all().order_by('-create_date')
    serializer_class = GetProjectFileSerializer
    # permission_classes = [IsUserAccess]

class ProjectFileCreateView(generics.CreateAPIView):
    queryset = ProjectFile.objects.all()
    serializer_class = CreateProjectFileSerializer
    # permission_classes = [IsUserAccess]
    
    def perform_create(self, serializer):
        serializer.save(uploader=self.request.user)

class ProjectFileUpdateView(generics.UpdateAPIView):
    queryset = ProjectFile.objects.all()
    serializer_class = CreateProjectFileSerializer
    # permission_classes = [IsUserAccess]
    
class ProjectFileDeleteView(generics.DestroyAPIView):
    queryset = ProjectFile.objects.all()
    serializer_class = GetProjectFileSerializer
    # permission_classes = [IsUserAccess]
    