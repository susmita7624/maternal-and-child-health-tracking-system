from django.urls import path
from . import views

urlpatterns = [
    path('', views.mother_list, name='mother_list'),
    path('register/', views.mother_register, 
         name='mother_register'),
    path('<int:pk>/', views.mother_detail, 
         name='mother_detail'),
    path('<int:pk>/delete/', views.mother_delete, 
         name='mother_delete'),
]