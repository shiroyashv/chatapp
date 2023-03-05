from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'), max_length=32,
        unique=True,
    )
    phone_number = models.CharField(
        _('phone number'), max_length=16,
        null=True, blank=True,
        unique=True,
        )
    name = models.CharField(
        _('name'), max_length=64,
        null=True, blank=True,
    )
    avatar = models.ImageField(
        _('avatar'),
        upload_to='avatars/',
        null=True, blank=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return f'/user/{self.username}/'
