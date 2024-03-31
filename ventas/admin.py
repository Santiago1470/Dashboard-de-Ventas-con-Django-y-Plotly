from django.contrib import admin
from ventas import models

@admin.register(models.Barrio)
class BarriosAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "ubicacion"]
@admin.register(models.Venta)  
class VentasAdmin(admin.ModelAdmin):
    list_display = ["id", "cantidad", "barrio"]
