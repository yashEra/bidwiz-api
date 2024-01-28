from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
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
class User(AbstractBaseUser):
    name = models.CharField(max_length=256, null = True)
    email = models.EmailField(max_length=200, primary_key=True,unique = True)
    password = models.CharField(max_length=1024)
    
    birth_date = models.CharField(max_length=30, null=True)
    avatar = models.ImageField(upload_to=upload_to, default="user/default_user.svg")
    username = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.name

    def has_module_perms(self, app_lable):
        return True

    def has_perm(self, perm, obj=None):
        return True

class Items(models.Model):
    item_id = models.CharField(max_length = 50 , primary_key = True)
    item_name = models.CharField(max_length = 256)
    category = models.CharField(max_length = 256)
    start_bid_price = models.CharField(max_length = 10)
    current_max_bid = models.CharField(max_length = 10)
    end_date = models.CharField(max_length = 10)
    description = models.DateField(max_length = 1024)
    reviews = models.PositiveSmallIntegerField(default = 0)
    reviews_score = models.PositiveSmallIntegerField(default = 0)
    cover_image = models.ImageField(upload_to=upload_to , default="items/default.png")
    imageone = models.ImageField(upload_to=upload_to , default="items/default.png")
    imagetwo = models.ImageField(upload_to=upload_to , default="items/default.png")
    imagethree = models.ImageField(upload_to=upload_to , default="items/default.png")

    REQUIRED_FIELDS = [item_name , item_name , start_bid_price , category , end_date , cover_image , description]