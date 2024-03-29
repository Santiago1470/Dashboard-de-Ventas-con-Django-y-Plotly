
from django.contrib import admin
from django.urls import path
from inventario.views import saludo
from inventario.views import inicio

urlpatterns = [
    path('', inicio),
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
]
