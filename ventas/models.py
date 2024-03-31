from django.db import models

class Barrio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    ubicacion = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre
    
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    def __int__(self):
        return self.id