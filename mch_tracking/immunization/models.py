from django.db import models
from children.models import Child

class Immunization(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=100)
    dose = models.CharField(max_length=50)
    vaccination_date = models.DateField()
    next_due_date = models.DateField(null=True, blank=True)
    given_by = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.child.child_name} - {self.vaccine_name}"