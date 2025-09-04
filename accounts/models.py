from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
import uuid

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_confirmed_email = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Token(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='auth_token')
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.token)

    class Meta:
        db_table = "auth_token"
        verbose_name = "Token"
        verbose_name_plural = "Tokens"
