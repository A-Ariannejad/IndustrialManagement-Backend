
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from CustomUserPermissions.models import CustomUserPermission

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        permission = CustomUserPermission.objects.filter(name='SuperAdmin', add_subOrganization=True, add_manager=True, add_project=True, view=True).first()
        if permission:
            extra_fields.setdefault('user_permissions', permission)
        else:
            extra_fields.setdefault('user_permissions', CustomUserPermission.objects.create(name='SuperAdmin', add_subOrganization=True, add_manager=True, add_project=True, view=True))
        User_permission = CustomUserPermission.objects.filter(name='User', add_subOrganization=False, add_manager=False, add_project=False, view=False).first()
        if not User_permission:
            CustomUserPermission.objects.create(name='User', add_subOrganization=False, add_manager=False, add_project=False, view=False)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=60, blank=True, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    user_permissions = models.ForeignKey(CustomUserPermission, on_delete=models.CASCADE, null=True, blank=True)
    #############################################################################
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    #############################################################################
    objects = UserManager()

    USERNAME_FIELD = 'email'

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
