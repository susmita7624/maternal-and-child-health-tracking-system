from django.shortcuts import render, redirect
from .models import Immunization
from children.models import Child

def immunization_list(request):
    records = Immunization.objects.all()
    return render(request, 'immunization/list.html',
                 {'records': records})

def immunization_add(request):
    if request.method == 'POST':
        Immunization.objects.create(
            child_id=request.POST['child'],
            vaccine_name=request.POST['vaccine_name'],
            dose=request.POST['dose'],
            vaccination_date=request.POST['vaccination_date'],
            next_due_date=request.POST['next_due_date'],
            given_by=request.POST['given_by'],
        )
        return redirect('immunization_list')
    children = Child.objects.all()
    return render(request, 'immunization/add.html',
                 {'children': children})
