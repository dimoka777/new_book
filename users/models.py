from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    user_phone = models.CharField(max_length=50, verbose_name='+996 555 55-55-55')
    is_active = models.BooleanField(default=False, verbose_name='Are you driver')
