from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


# upload file and rename
def upload_to(instance, filename):
    return 'items/{filename}.{ext}'.format(filename=instance.pk, ext=filename.split('.')[-1])


class Standard(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


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
