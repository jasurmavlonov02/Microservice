from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_superuser = models.BooleanField(default=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='users', null=True, verbose_name='роль')

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]


class Role(models.Model):
    name = models.CharField(max_length=255, verbose_name='Названия рольов ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Роли'
        verbose_name = 'Роль'
