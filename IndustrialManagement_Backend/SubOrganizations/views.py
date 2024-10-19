from .serializers import CreateSubOrganizationSerializer
from IndustrialManagement_Backend.serializers import GetSubOrganizationSerializer, GetSelectSubOrganizationSerializer, CustomValidation
from Projects.models import CustomUser, Project
from .models import SubOrganization, Organization
from django.db.models import Prefetch
from rest_framework import generics, viewsets, permissions, status
from django.db.models import Q

def subOrganization_permission_type_queryset(self):
        user = self.request.user
        if user.admin:
            return self.queryset
        owner_sub_orgs = SubOrganization.objects.filter(owner=user)
        project_owner_sub_orgs = SubOrganization.objects.filter(project__owner=user)
        related_project_sub_orgs = []
        if user.crud_project:
            related_project_sub_orgs = SubOrganization.objects.filter(project__in=user.projects.all())
        queryset = self.queryset.filter(
            Q(id__in=owner_sub_orgs) |
            Q(id__in=project_owner_sub_orgs) |
            Q(id__in=related_project_sub_orgs)
        )
        return queryset.distinct()  

class SubOrganizationShowView(generics.RetrieveAPIView):
    queryset = SubOrganization.objects.prefetch_related(Prefetch('customuser_set', queryset=CustomUser.objects.prefetch_related(Prefetch('project_set', queryset=Project.objects.all())))).all()
    serializer_class = GetSubOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return subOrganization_permission_type_queryset(self=self)

class SubOrganizationViewSet(viewsets.ModelViewSet):
    queryset = SubOrganization.objects.prefetch_related(Prefetch('customuser_set', queryset=CustomUser.objects.prefetch_related(Prefetch('project_set', queryset=Project.objects.all())))).all().order_by('-create_date')
    serializer_class = GetSubOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return subOrganization_permission_type_queryset(self=self) 
        
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
class SelectSubOrganizationViewSet(viewsets.ModelViewSet):
    queryset = SubOrganization.objects.all()
    serializer_class = GetSelectSubOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return subOrganization_permission_type_queryset(self=self)  

class SubOrganizationCreateView(generics.CreateAPIView):
    queryset = SubOrganization.objects.all()
    serializer_class = CreateSubOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return subOrganization_permission_type_queryset(self=self) 
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def perform_create(self, serializer):
        user = self.request.user
        organization_id = self.request.data.get('organization')
        organization = Organization.objects.get(id=organization_id)
        if user.admin or organization.owner == user:
            serializer.save(owner=user, organization=organization)
        else:
            raise CustomValidation("شما اجازه این کار را ندارید", "", status_code=status.HTTP_401_UNAUTHORIZED)

class SubOrganizationUpdateView(generics.UpdateAPIView):
    queryset = SubOrganization.objects.all()
    serializer_class = CreateSubOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return subOrganization_permission_type_queryset(self=self) 
    
class SubOrganizationDeleteView(generics.DestroyAPIView):
    queryset = SubOrganization.objects.all()
    serializer_class = GetSubOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return subOrganization_permission_type_queryset(self=self)
    