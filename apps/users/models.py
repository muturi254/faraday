from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users Must have an email")
        user = self.model(
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True
    )
    is_student = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does this user have a specific permission"
        return True

    def has_module_perms(self, app_label):  
        "Does this user have a specific permission"
        return True


class UserProfile(models.Model):

    LEVELS = [
        (1, "level one"),
        (2, "level two")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    preferred_name  = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile-images')
    dicord_name = models.CharField(max_length=100)
    github_username = models.CharField(max_length=100)
    codepen_username = models.CharField(max_length=100)
    fcc_profile_url = models.CharField(max_length=255)
    current_level = models.IntegerField(choices=LEVELS)
    phone = models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'