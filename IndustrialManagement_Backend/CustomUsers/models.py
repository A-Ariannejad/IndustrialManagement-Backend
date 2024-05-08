
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from CustomUserPermissions.models import CustomUserPermission
from phonenumber_field.modelfields import PhoneNumberField

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
    social_id = models.CharField(max_length=30, blank=True)
    phone_number = PhoneNumberField(blank=True)
    EDUCATION_CHOICES = (
        ('BSc', 'BSc'),
        ('Ms', 'Ms'),
        ('PhD', 'PhD'),
        ('Prof', 'Prof'),
    )
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    user_permissions = models.ForeignKey(CustomUserPermission, on_delete=models.CASCADE, null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
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
        return self.email


class LogicUser:
    def get_user(request):
        user = None
        try:
            id = request.user.id
            user = CustomUser.objects.get(id=id)
        except:
            pass
        return user
