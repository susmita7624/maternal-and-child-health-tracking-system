from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from mothers.models import Mother

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/list.html',
                 {'appointments': appointments})

def appointment_add(request):
    if request.method == 'POST':
        Appointment.objects.create(
            mother_id=request.POST['mother'],
            appointment_date=request.POST['appointment_date'],
            appointment_type=request.POST['appointment_type'],
            notes=request.POST['notes'],
        )
        return redirect('appointment_list')
    mothers = Mother.objects.all()
    return render(request, 'appointments/add.html',
                 {'mothers': mothers})