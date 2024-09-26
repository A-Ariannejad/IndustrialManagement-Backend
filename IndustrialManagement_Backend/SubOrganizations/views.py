from .serializers import CreateSubOrganizationSerializer
from IndustrialManagement_Backend.serializers import GetSubOrganizationSerializer
from Projects.models import CustomUser, Project
from CustomUserPermissions.views import IsUserAccess
from .models import SubOrganization
from django.db.models import Prefetch
from rest_framework import generics, viewsets

class SubOrganizationShowView(generics.RetrieveAPIView):
    queryset = SubOrganization.objects.all()
    serializer_class = GetSubOrganizationSerializer
    # permission_classes = [IsUserAccess]
    lookup_field = 'id'

class SubOrganizationViewSet(viewsets.ModelViewSet):
    queryset = SubOrganization.objects.prefetch_related(Prefetch('project_owners', queryset=CustomUser.objects.prefetch_related(Prefetch('projects', queryset=Project.objects.all())))).all().order_by('-create_date')
    serializer_class = GetSubOrganizationSerializer
    # permission_classes = [IsUserAccess]

class SubOrganizationCreateView(generics.CreateAPIView):
    queryset = SubOrganization.objects.all()
    serializer_class = CreateSubOrganizationSerializer
    # permission_classes = [IsUserAccess]

class SubOrganizationUpdateView(generics.UpdateAPIView):
    queryset = SubOrganization.objects.all()
    serializer_class = CreateSubOrganizationSerializer
    # permission_classes = [IsUserAccess]
    
class SubOrganizationDeleteView(generics.DestroyAPIView):
    queryset = SubOrganization.objects.all()
    serializer_class = GetSubOrganizationSerializer
    # permission_classes = [IsUserAccess]
    