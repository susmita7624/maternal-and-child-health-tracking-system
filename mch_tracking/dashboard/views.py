from django.shortcuts import render
from mothers.models import Mother        # ← from mothers
from children.models import Child        # ← from children
from appointments.models import Appointment
from emergency.models import Emergency

def index(request):
    context = {
        'total_mothers': Mother.objects.count(),
        'total_children': Child.objects.count(),
        'total_appointments': Appointment.objects.count(),
        'total_emergencies': Emergency.objects.filter(
                             status='Reported').count(),
    }
    return render(request, 'dashboard/index.html', context)