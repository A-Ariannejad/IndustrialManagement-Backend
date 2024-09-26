from .serializers import CreateOrganizationSerializer
from IndustrialManagement_Backend.serializers import GetOrganizationSerializer
from CustomUserPermissions.views import IsUserAccess
from .models import Organization
from rest_framework import generics, viewsets

class OrganizationShowView(generics.RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = GetOrganizationSerializer
    # permission_classes = [IsUserAccess]
    lookup_field = 'id'

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by('-create_date')
    serializer_class = GetOrganizationSerializer
    # permission_classes = [IsUserAccess]

class OrganizationCreateView(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = CreateOrganizationSerializer
    # permission_classes = [IsUserAccess]

class OrganizationUpdateView(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = CreateOrganizationSerializer
    # permission_classes = [IsUserAccess]
    
class OrganizationDeleteView(generics.DestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = GetOrganizationSerializer
    # permission_classes = [IsUserAccess]
    