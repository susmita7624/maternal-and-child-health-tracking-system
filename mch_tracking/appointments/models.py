from django.db import models
from mothers.models import Mother

class Appointment(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_type = models.CharField(max_length=20, choices=[
        ('ANC', 'ANC'),
        ('PNC', 'PNC'),
        ('Immunization', 'Immunization'),
        ('Other', 'Other'),
    ])
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Missed', 'Missed'),
    ], default='Scheduled')

    def __str__(self):
        return f"{self.mother.name} - {self.appointment_type}"