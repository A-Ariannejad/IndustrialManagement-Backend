from .serializers import CreatePieScaleSerializer, GetPieScaleWithoutProjectSerializer
from IndustrialManagement_Backend.serializers import GetPieScaleSerializer, CustomValidation, scale_type_queryset
from .models import PieScale, Project
from rest_framework import generics, viewsets, status, permissions
from django.db.models import Q

class PieScaleShowView(generics.RetrieveAPIView):
    queryset = PieScale.objects.all()
    serializer_class = GetPieScaleSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return scale_type_queryset(self=self)

class PieScaleViewSet(viewsets.ModelViewSet):
    queryset = PieScale.objects.all().order_by('-create_date')
    serializer_class = GetPieScaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return scale_type_queryset(self=self).all()

class PieScaleShowByProjectViewSet(viewsets.ModelViewSet):
    serializer_class = GetPieScaleWithoutProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        self.queryset = PieScale.objects.all()
        queryset = scale_type_queryset(self=self).all()
        project_id = self.kwargs['pk']
        return queryset.filter(project_id=project_id).order_by('-create_date')

class PieScaleCreateView(generics.CreateAPIView):
    queryset = PieScale.objects.all()
    serializer_class = CreatePieScaleSerializer
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

class PieScaleUpdateView(generics.UpdateAPIView):
    queryset = PieScale.objects.all()
    serializer_class = CreatePieScaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        pieScale_id = self.kwargs['pk']
        pieScale = PieScale.objects.filter(id=pieScale_id).first()
        if not pieScale:
            raise CustomValidation("داده یافت نشد", "", status_code=status.HTTP_404_NOT_FOUND)
        if not user.admin and not (pieScale.project.owner == user or pieScale.project in user.projects.all()):            
            raise CustomValidation("شما اجازه این کار را ندارید", "", status_code=status.HTTP_403_FORBIDDEN)
        return super().perform_update(serializer)
    
class PieScaleDeleteView(generics.DestroyAPIView):
    queryset = PieScale.objects.all()
    serializer_class = GetPieScaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        user = self.request.user
        pieScale_id = self.kwargs['pk']
        pieScale = PieScale.objects.filter(id=pieScale_id).first()
        if not pieScale:
            raise CustomValidation("داده یافت نشد", "", status_code=status.HTTP_404_NOT_FOUND)
        if not user.admin and not (pieScale.project.owner == user or pieScale.project in user.projects.all()):            
            raise CustomValidation("شما اجازه این کار را ندارید", "", status_code=status.HTTP_403_FORBIDDEN)
        return super().perform_destroy(instance)
    