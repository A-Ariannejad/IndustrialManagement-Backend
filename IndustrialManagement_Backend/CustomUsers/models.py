
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from CustomUserPermissions.models import CustomUserPermission
from phonenumber_field.modelfields import PhoneNumberField
# from SubOrganizations.models import SubOrganization

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        permission = CustomUserPermission.objects.filter(name='SuperAdmin', add_subOrganization=True, add_manager=True, add_project=True, user_access=True).first()
        if permission:
            extra_fields.setdefault('user_permissions', permission)
        else:
            extra_fields.setdefault('user_permissions', CustomUserPermission.objects.create(name='SuperAdmin', add_subOrganization=True, add_manager=True, add_project=True, user_access=True))
        User_permission = CustomUserPermission.objects.filter(name='User', add_subOrganization=False, add_manager=False, add_project=False, user_access=False).first()
        if not User_permission:
            CustomUserPermission.objects.create(name='User', add_subOrganization=False, add_manager=False, add_project=False, user_access=False)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50)
    nickname = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    social_id_number = models.CharField(max_length=30, blank=True)
    personal_id_number = models.CharField(max_length=30, blank=True)
    mobile_phone_number = PhoneNumberField(blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    EDUCATION_CHOICES = (
        ('BSc', 'BSc'),
        ('Ms', 'Ms'),
        ('PhD', 'PhD'),
        ('Prof', 'Prof'),
    )
    education_level = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    user_permissions = models.ForeignKey(CustomUserPermission, on_delete=models.CASCADE, null=False, blank=False)
    subOrganizations = models.ForeignKey('SubOrganizations.SubOrganization', on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    #############################################################################
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    #############################################################################
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    def __str__(self):
        return self.username

class LogicUser:
    def get_user(request):
        user = None
        try:
            id = request.user.id
            user = CustomUser.objects.get(id=id)
        except:
            pass
        return user
