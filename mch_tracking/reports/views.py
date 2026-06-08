from django.shortcuts import render
from mothers.models import Mother
from children.models import Child
from appointments.models import Appointment
from immunization.models import Immunization
from emergency.models import Emergency

def reports_index(request):
    context = {
        'total_mothers': Mother.objects.count(),
        'high_risk': Mother.objects.filter(
                     risk_level='High').count(),
        'total_children': Child.objects.count(),
        'total_appointments': Appointment.objects.count(),
        'missed_appointments': Appointment.objects.filter(
                               status='Missed').count(),
        'total_immunizations': Immunization.objects.count(),
        'total_emergencies': Emergency.objects.count(),
    }
    return render(request, 'reports/index.html', context)