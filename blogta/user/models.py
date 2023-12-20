from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from managers import CustomUserManager

class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    objects = CustomUserManager()

    class Meta:
        permissions = [("can_access_admin", "Can access admin panel"), ("add_article", "Can add articles")]