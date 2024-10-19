from .serializers import CreateRealScaleSerializer, GetRealScaleWithoutProjectSerializer
from IndustrialManagement_Backend.serializers import GetRealScaleSerializer, CustomValidation, scale_type_queryset
from .models import RealScale, Project
from rest_framework import generics, viewsets, permissions, status

class RealScaleShowView(generics.RetrieveAPIView):
    queryset = RealScale.objects.all()
    serializer_class = GetRealScaleSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    
    def get_queryset(self):
        return scale_type_queryset(self=self)

class RealScaleViewSet(viewsets.ModelViewSet):
    queryset = RealScale.objects.all().order_by('-create_date')
    serializer_class = GetRealScaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return scale_type_queryset(self=self)

class RealScaleShowByProjectViewSet(viewsets.ModelViewSet):
    serializer_class = GetRealScaleWithoutProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        self.queryset = RealScale.objects.all()
        queryset = scale_type_queryset(self=self)
        project_id = self.kwargs['pk']
        return queryset.filter(project_id=project_id).order_by('-create_date')

class RealScaleCreateView(generics.CreateAPIView):
    queryset = RealScale.objects.all()
    serializer_class = CreateRealScaleSerializer
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
        return super().perform_create(serializer)

class RealScaleUpdateView(generics.UpdateAPIView):
    queryset = RealScale.objects.all()
    serializer_class = CreateRealScaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        pieScale_id = self.kwargs['pk']
        pieScale = RealScale.objects.filter(id=pieScale_id).first()
        if not pieScale:
            raise CustomValidation("داده یافت نشد", "", status_code=status.HTTP_404_NOT_FOUND)
        if not user.admin and not (pieScale.project.owner == user or pieScale.project in user.projects.all()):            
            raise CustomValidation("شما اجازه این کار را ندارید", "", status_code=status.HTTP_403_FORBIDDEN)
        return super().perform_update(serializer)
    
class RealScaleDeleteView(generics.DestroyAPIView):
    queryset = RealScale.objects.all()
    serializer_class = GetRealScaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        user = self.request.user
        pieScale_id = self.kwargs['pk']
        pieScale = RealScale.objects.filter(id=pieScale_id).first()
        if not pieScale:
            raise CustomValidation("داده یافت نشد", "", status_code=status.HTTP_404_NOT_FOUND)
        if not user.admin and not (pieScale.project.owner == user or pieScale.project in user.projects.all()):            
            raise CustomValidation("شما اجازه این کار را ندارید", "", status_code=status.HTTP_403_FORBIDDEN)
        return super().perform_destroy(instance)
    