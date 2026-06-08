from django.db import models
from mothers.models import Mother

class Notification(models.Model):
    mother = models.ForeignKey(
        Mother, 
        on_delete=models.CASCADE
    )
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    sms_status = models.CharField(
        max_length=20,
        choices=[
            ('Sent', 'Sent'),
            ('Failed', 'Failed'),
            ('Pending', 'Pending'),
        ], 
        default='Pending'
    )

    def __str__(self):
        return f"SMS to {self.mother.name}"
