from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUsers(AbstractUser):
    user_photo = models.ImageField(upload_to='user/', blank=True,null=True)