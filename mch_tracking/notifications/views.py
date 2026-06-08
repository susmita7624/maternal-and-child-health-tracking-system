from django.shortcuts import render, redirect
from .models import Notification
from mothers.models import Mother

def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications/list.html',
                 {'notifications': notifications})

def send_notification(request):
    if request.method == 'POST':
        Notification.objects.create(
            mother_id=request.POST['mother'],
            message=request.POST['message'],
            sms_status='Pending',
        )
        return redirect('notification_list')
    mothers = Mother.objects.all()
    return render(request, 'notifications/send_sms.html',
                 {'mothers': mothers})