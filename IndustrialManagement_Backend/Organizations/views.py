from .serializers import CreateOrganizationSerializer
from IndustrialManagement_Backend.serializers import GetOrganizationSerializer, Organization, SubOrganization, CustomUser, Project
from CustomUsers.permissions import IsAdmin
from rest_framework import generics, viewsets, permissions
from django.db.models import Prefetch
from django.db.models import Q

def organization_permission_type_queryset(self):
    user = self.request.user
    if user.admin:
        return self.queryset
    owner_orgs = Organization.objects.filter(owner=user)
    owner_sub_orgs = Organization.objects.filter(suborganization__owner=user)
    project_owner_orgs = Organization.objects.filter(suborganization__project__owner=user)
    related_project_orgs = []
    if user.crud_project:
        related_project_orgs = Organization.objects.filter(suborganization__project__in=user.projects.all())
    queryset = self.queryset.filter(
        Q(id__in=owner_orgs) |
        Q(id__in=owner_sub_orgs) |
        Q(id__in=project_owner_orgs) |
        Q(id__in=related_project_orgs)
    )
    return queryset.distinct()

class OrganizationShowView(generics.RetrieveAPIView):
    queryset = Organization.objects.prefetch_related(
    Prefetch(
        'suborganization_set',
        queryset=SubOrganization.objects.prefetch_related(
            Prefetch(
                'customuser_set',
                queryset=CustomUser.objects.prefetch_related(
                    Prefetch('project_set', queryset=Project.objects.all())
                )
            )
        )
    )).all()
    serializer_class = GetOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.prefetch_related(
    Prefetch(
        'suborganization_set',
        queryset=SubOrganization.objects.prefetch_related(
            Prefetch(
                'customuser_set',
                queryset=CustomUser.objects.prefetch_related(
                    Prefetch('project_set', queryset=Project.objects.all())
                )
            )
        )
    )).all().order_by('-create_date')
    serializer_class = GetOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return organization_permission_type_queryset(self=self)

class OrganizationCreateView(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = CreateOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get_queryset(self):
        return organization_permission_type_queryset(self=self)

class OrganizationUpdateView(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = CreateOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get_queryset(self):
        return organization_permission_type_queryset(self=self)
    
class OrganizationDeleteView(generics.DestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = GetOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get_queryset(self):
        return organization_permission_type_queryset(self=self)
    