from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('health_worker', 'Health Worker'),
        ('mother', 'Mother'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
