from django.shortcuts import render, redirect
from .models import Emergency
from mothers.models import Mother

def emergency_list(request):
    emergencies = Emergency.objects.all()
    return render(request, 'emergency/list.html',
                 {'emergencies': emergencies})

def emergency_report(request):
    if request.method == 'POST':
        Emergency.objects.create(
            mother_id=request.POST['mother'],
            description=request.POST['description'],
            action_taken=request.POST['action_taken'],
        )
        return redirect('emergency_list')
    mothers = Mother.objects.all()
    return render(request, 'emergency/report.html',
                 {'mothers': mothers})