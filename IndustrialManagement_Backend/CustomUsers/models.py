
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from CustomUserPermissions.models import CustomUserPermission

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The email field must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        permission = CustomUserPermission.objects.filter(name='SuperAdmin', is_controller=True, is_viewer=True, is_calculator=True, is_supporter=True).first()
        if permission:
            extra_fields.setdefault('user_permissions', permission)
        else:
            extra_fields.setdefault('user_permissions', CustomUserPermission.objects.create(name='SuperAdmin', is_controller=True, is_viewer=True, is_calculator=True, is_supporter=True))
        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=60, blank=False, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    user_permissions = models.ForeignKey(CustomUserPermission, on_delete=models.CASCADE, null=True, blank=True)
    #############################################################################
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    #############################################################################
    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']


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
