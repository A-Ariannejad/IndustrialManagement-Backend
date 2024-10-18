from .serializers import CreateProjectSerializer
from IndustrialManagement_Backend.serializers import GetProjectSerializer
from .models import Project
from rest_framework import generics, viewsets, permissions
from django.db.models import Q

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
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return project_permission_type_queryset(self=self)

class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = CreateProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return project_permission_type_queryset(self=self)
    
class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = GetProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return project_permission_type_queryset(self=self)
    