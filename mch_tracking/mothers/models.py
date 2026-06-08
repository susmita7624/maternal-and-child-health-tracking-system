from django.db import models

class Mother(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=5)
    registration_date = models.DateField(auto_now_add=True)
    trimester = models.IntegerField(default=1)
    risk_level = models.CharField(max_length=20, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ], default='Low')

    def __str__(self):
        return self.name
