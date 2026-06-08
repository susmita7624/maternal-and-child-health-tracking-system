from django.urls import path
from . import views

urlpatterns = [
    path('', views.emergency_list, 
         name='emergency_list'),
    path('report/', views.emergency_report, 
         name='emergency_report'),
]