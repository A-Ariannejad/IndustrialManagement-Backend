from .serializers import CreateProjectFileSerializer, GetProjectFileWithoutProjectSerializer
from IndustrialManagement_Backend.serializers import GetProjectFileSerializer, CustomValidation, scale_type_queryset
from .models import ProjectFile, Project
from rest_framework import generics, viewsets, permissions, status

class ProjectFileShowView(generics.RetrieveAPIView):
    queryset = ProjectFile.objects.all()
    serializer_class = GetProjectFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return scale_type_queryset(self=self)

class ProjectFileViewSet(viewsets.ModelViewSet):
    queryset = ProjectFile.objects.all().order_by('-create_date')
    serializer_class = GetProjectFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return scale_type_queryset(self=self).all()
    
class ProjectFileShowByProjectViewSet(viewsets.ModelViewSet):
    serializer_class = GetProjectFileWithoutProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        self.queryset = ProjectFile.objects.all()
        queryset = scale_type_queryset(self=self).all()
        project_id = self.kwargs['pk']
        return queryset.filter(project_id=project_id).order_by('-create_date')

class ProjectFileCreateView(generics.CreateAPIView):
    queryset = ProjectFile.objects.all()
    serializer_class = CreateProjectFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def perform_create(self, serializer):
        user = self.request.user
        project_id = self.request.data.get('project')
        project = Project.objects.filter(id=project_id).first()
        if not project:
            raise CustomValidation("پروژه یافت نشد", "", status_code=status.HTTP_404_NOT_FOUND)
        if not user.admin and not (project.owner == user or project in user.projects.all()):            
            raise CustomValidation("شما اجازه این کار را ندارید", "", status_code=status.HTTP_403_FORBIDDEN)
        serializer.save(uploader=self.request.user)

class ProjectFileUpdateView(generics.UpdateAPIView):
    queryset = ProjectFile.objects.all()
    serializer_class = CreateProjectFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_update(self, serializer):
        user = self.request.user
        pieScale_id = self.kwargs['pk']
        pieScale = ProjectFile.objects.filter(id=pieScale_id).first()
        if not pieScale:
            raise CustomValidation("داده یافت نشد", "", status_code=status.HTTP_404_NOT_FOUND)
        if not user.admin and not (pieScale.project.owner == user or pieScale.project in user.projects.all()):            
            raise CustomValidation("شما اجازه این کار را ندارید", "", status_code=status.HTTP_403_FORBIDDEN)
        return super().perform_update(serializer)
    
class ProjectFileDeleteView(generics.DestroyAPIView):
    queryset = ProjectFile.objects.all()
    serializer_class = GetProjectFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        user = self.request.user
        pieScale_id = self.kwargs['pk']
        pieScale = ProjectFile.objects.filter(id=pieScale_id).first()
        if not pieScale:
            raise CustomValidation("داده یافت نشد", "", status_code=status.HTTP_404_NOT_FOUND)
        if not user.admin and not (pieScale.project.owner == user or pieScale.project in user.projects.all()):            
            raise CustomValidation("شما اجازه این کار را ندارید", "", status_code=status.HTTP_403_FORBIDDEN)
        return super().perform_destroy(instance)
    