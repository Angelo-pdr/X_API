from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User (AbstractBaseUser):
    fullName = models.CharField(unique=True, max_length=150)
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    user_active = models.BooleanField(default=True)
    user_adm = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'username', 'fullName']

    def __str__(self) -> str:
        return f'{self.username} - {self.email}'
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perm(self, perm, obj = None):
        return True
    
    @property
    def is_staff(self):
        return self.user_adm
