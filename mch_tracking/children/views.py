from django.shortcuts import render, redirect, get_object_or_404
from .models import Child

def child_list(request):
    children = Child.objects.all()
    return render(request, 'children/list.html', 
                 {'children': children})

def child_register(request):
    if request.method == 'POST':
        Child.objects.create(
            mother_id=request.POST['mother'],
            child_name=request.POST['child_name'],
            gender=request.POST['gender'],
            birth_weight=request.POST['birth_weight'],
            date_of_birth=request.POST['date_of_birth'],
        )
        return redirect('child_list')
    from mothers.models import Mother
    mothers = Mother.objects.all()
    return render(request, 'children/register.html',
                 {'mothers': mothers})

def child_detail(request, pk):
    child = get_object_or_404(Child, pk=pk)
    return render(request, 'children/detail.html',
                 {'child': child})

