from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(max_length=50, choices=[
        ('Admin', 'Admin'),
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Health Worker', 'Health Worker'),
    ], default='Nurse')
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username