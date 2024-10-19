from .serializers import CreateProjectSerializer
from IndustrialManagement_Backend.serializers import GetProjectSerializer, CustomValidation
from .models import Project
from rest_framework import generics, viewsets, permissions, status
from django.db.models import Q
from CustomUsers.permissions import IsAdmin

def project_permission_type_queryset(self):
        user = self.request.user
        if user.admin:
            return self.queryset
        owner_projects = Project.objects.filter(owner=user)
        related_projects = []
        if user.crud_project:
            related_projects = Project.objects.filter(id__in=user.projects.all())
        queryset = self.queryset.filter(
            Q(id__in=owner_projects) |
            Q(id__in=related_projects)
        )
        return queryset.distinct() 

class ProjectShowView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = GetProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return project_permission_type_queryset(self=self)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-create_date')
    serializer_class = GetProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return project_permission_type_queryset(self=self)
    
class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = CreateProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get_queryset(self):
        return project_permission_type_queryset(self=self)

class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = CreateProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return project_permission_type_queryset(self=self)
    
    def perform_update(self, serializer):
        user = self.request.user
        project_id = self.kwargs['pk']
        project = Project.objects.get(id=project_id)
        if user.admin or project.owner == user or user.crud_project and project in user.projects.all():
            return super().perform_update(serializer)
        else:
            raise CustomValidation("شما اجازه این کار را ندارید", "", status_code=status.HTTP_401_UNAUTHORIZED)
    
class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = GetProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return project_permission_type_queryset(self=self)
    
    def perform_destroy(self, instance):
        user = self.request.user
        project_id = self.kwargs['pk']
        project = Project.objects.get(id=project_id)
        if user.admin or project.owner == user or user.crud_project and project in user.projects.all():
            return super().perform_destroy(instance)
        else:
            raise CustomValidation("شما اجازه این کار را ندارید", "", status_code=status.HTTP_401_UNAUTHORIZED)
    