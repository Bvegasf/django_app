from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    name = models.CharField(max_length = 100, blank=True, null= True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)

    class Meta:
        db_table = 'User'
    
    def __str__(self):
        return f'{self.email}'

