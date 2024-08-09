from .serializers import GetSubOrganizationSerializer, CreateSubOrganizationSerializer
from CustomUserPermissions.views import IsUserAccess
from .models import SubOrganization
from rest_framework import generics, viewsets

class SubOrganizationShowView(generics.RetrieveAPIView):
    queryset = SubOrganization.objects.all()
    serializer_class = GetSubOrganizationSerializer
    # permission_classes = [IsUserAccess]
    lookup_field = 'id'

class SubOrganizationViewSet(viewsets.ModelViewSet):
    queryset = SubOrganization.objects.all().order_by('-create_date')
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
    