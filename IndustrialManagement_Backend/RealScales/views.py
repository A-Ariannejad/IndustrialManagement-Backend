from .serializers import CreateRealScaleSerializer, GetRealScaleWithoutProjectSerializer
from IndustrialManagement_Backend.serializers import GetRealScaleSerializer
from .models import RealScale, Project
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
        user = self.request.user
        project_id = self.kwargs['pk']
        if user.admin:
            return RealScale.objects.filter(project=project_id).order_by('-create_date')
        project = Project.objects.filter(id=project_id).first()
        if not project:
            return RealScale.objects.none()
        if project.owner == user:
            return RealScale.objects.filter(project=project).order_by('-create_date')
        if project.subOrganization.owner == user:
            return RealScale.objects.filter(project=project).order_by('-create_date')
        if project in user.projects.all() and user.crud_project:
            return RealScale.objects.filter(project=project).order_by('-create_date')
        return RealScale.objects.none()

class RealScaleCreateView(generics.CreateAPIView):
    queryset = RealScale.objects.all()
    serializer_class = CreateRealScaleSerializer
    # permission_classes = [IsUserAccess]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class RealScaleUpdateView(generics.UpdateAPIView):
    queryset = RealScale.objects.all()
    serializer_class = CreateRealScaleSerializer
    # permission_classes = [IsUserAccess]
    
class RealScaleDeleteView(generics.DestroyAPIView):
    queryset = RealScale.objects.all()
    serializer_class = GetRealScaleSerializer
    # permission_classes = [IsUserAccess]
    