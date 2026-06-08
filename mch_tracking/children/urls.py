from django.urls import path
from . import views

urlpatterns = [
    path('', views.child_list, name='child_list'),
    path('register/', views.child_register, 
         name='child_register'),
    path('<int:pk>/', views.child_detail, 
         name='child_detail'),
]