from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('mothers/', include('mothers.urls')),
    path('children/', include('children.urls')),
    path('appointments/', include('appointments.urls')),
    path('immunization/', include('immunization.urls')),
    path('emergency/', include('emergency.urls')),
    path('notifications/', include('notifications.urls')),
    path('reports/', include('reports.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('dashboard.urls')),  # homepage
]
