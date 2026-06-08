from django.urls import path
from . import views

urlpatterns = [
    path('', views.immunization_list, 
         name='immunization_list'),
    path('add/', views.immunization_add, 
         name='immunization_add'),
]