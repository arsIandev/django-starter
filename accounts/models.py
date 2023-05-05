from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .managers import UserManager 


class User(AbstractUser):
    username = first_name = last_name = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(_("email address"), unique=True)
    is_active = models.BooleanField(_("active"), default=True)
    avatar = models.ImageField(upload_to='accounts/avatar/', blank=True, null=True)
    objects = UserManager()
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.name
