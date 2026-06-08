from django.db import models
from mothers.models import Mother

class Child(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
    ])
    birth_weight = models.FloatField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.child_name

