from django.db import models
from mothers.models import Mother

class Emergency(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE)
    reported_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    action_taken = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[
        ('Reported', 'Reported'),
        ('Resolved', 'Resolved'),
    ], default='Reported')

    def __str__(self):
        return f"Emergency - {self.mother.name}"
