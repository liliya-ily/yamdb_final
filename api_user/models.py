from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomSuperUser(BaseUserManager):

    # def create_user(self, email, password=None, **kwargs):
    #     user = self.model(email=email, **kwargs)
    #     user.save(using=self._db)
    #     return user

    # def create_superuser(self, email, password, **kwargs):
    #     user = self.model(email=email,
    #                       is_staff=True,
    #                       is_superuser=True, **kwargs)
    #     user.save(using=self._db)
    #     return user
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Неоходимо ввести адрес электронной почты')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    STATUS = [
        ('user', 'user'),
        ('admin', 'admin'),
        ('moderator', 'moderator'),
    ]
    role = models.CharField(max_length=9, choices=STATUS, default='user')
    bio = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=250, blank=True, null=True, unique=True)
    confirm_code = models.CharField(max_length=250, default='12345678')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomSuperUser()
