
from django.contrib import admin
from django.urls import path
from ventas import views


urlpatterns = [
    path('', views.inicio),
    path('admin/', admin.site.urls),
    path('visualizacion/', views.mostrarVentas),
]
