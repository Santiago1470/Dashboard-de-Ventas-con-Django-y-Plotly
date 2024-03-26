from django.contrib import admin
from inventario.models import Carro

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    #fields = ["marca", "cantidad"]
    list_display = ["marca", "cantidad", "pais"]

#admin.site.register(Carro, CarroAdmin)