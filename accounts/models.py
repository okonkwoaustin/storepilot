from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from .manager import UserManager

class CustomUser(AbstractUser):
    """Custom user"""
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    phone_number = models.CharField(max_length=11, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]
    objects = UserManager()

    def __str__(self):
        return self.email
    

class Store(models.Model):
    """A Store model"""
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="store_logos/", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)