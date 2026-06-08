from django.shortcuts import render, redirect, get_object_or_404
from .models import Mother

def mother_list(request):
    mothers = Mother.objects.all()
    return render(request, 'mothers/list.html', 
                 {'mothers': mothers})

def mother_register(request):
    if request.method == 'POST':
        Mother.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            blood_group=request.POST['blood_group'],
            trimester=request.POST['trimester'],
            risk_level=request.POST['risk_level'],
        )
        return redirect('mother_list')
    return render(request, 'mothers/register.html')

def mother_detail(request, pk):
    mother = get_object_or_404(Mother, pk=pk)
    return render(request, 'mothers/detail.html', 
                 {'mother': mother})

def mother_delete(request, pk):
    mother = get_object_or_404(Mother, pk=pk)
    mother.delete()
    return redirect('mother_list')