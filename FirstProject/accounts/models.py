from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100, unique=True)
    profile_image = models.ImageField(upload_to="profile", null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    # this is use to provide login by phone_numer instead of username
    USERNAME_FIELD = "phone_number"
    # this is use to required your custom filed
    REQUIRED_FIELDS = []
    objects = UserManager()