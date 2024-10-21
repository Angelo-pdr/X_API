from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, email, fullName, password=None, **extra_fields):
        if not username:
            raise ValueError('O nome de usuário é obrigatório')
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, fullName=fullName, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, fullName, password=None, **extra_fields):
        extra_fields.setdefault('user_adm', True)
        extra_fields.setdefault('user_active', True)

        if extra_fields.get('user_adm') is not True:
            raise ValueError('Superuser precisa ter user_adm=True.')
        return self.create_user(username, email, fullName, password, **extra_fields)

class User (AbstractBaseUser):
    objects = UserManager()

    fullName = models.CharField(unique=True, max_length=150)
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    user_active = models.BooleanField(default=True)
    user_adm = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','fullName']

    def __str__(self) -> str:
        return f'{self.username} - {self.email}'
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perm(self, perm, obj = None):
        return True
    
    @property
    def is_staff(self):
        return self.user_adm
