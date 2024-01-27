from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models


# upload file and rename
def upload_to(instance, filename):
    return 'items/{filename}.{ext}'.format(filename=instance.pk, ext=filename.split('.')[-1])


class Standard(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


# user mode manager
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email is not given.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active',True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff = true')

        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser = true')
        return self.create_user(email, password, **extra_fields)


# user model : its override the djangp abstract user
class User(AbstractUser):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=200, primary_key=True)
    password = models.CharField(max_length=1024)
    birth_date = models.CharField(max_length=30, null=True)
    avatar = models.ImageField(upload_to=upload_to, default="user/default_user.svg")
    username = models.CharField(max_length=256, null=True)
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [name, email, password]

    def __str__(self):
        return self.name

    def has_module_perms(self, app_lable):
        return True

    def has_perm(self, perm, obj=None):
        return True
