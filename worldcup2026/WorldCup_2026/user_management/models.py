from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='photos/users', blank=True, null=True, verbose_name='Imágen')
    phone = models.CharField(null=True, max_length=10, verbose_name='Teléfono')
