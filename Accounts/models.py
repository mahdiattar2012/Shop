from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    code = models.CharField(max_length=6)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
