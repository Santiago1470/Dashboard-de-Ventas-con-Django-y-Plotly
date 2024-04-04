from django.db import models

class Barrio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    ubicacion = models.CharField(max_length=120)
    localidad = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    eleccion = [
        ('ENERO', 'Enero'),
        ('FEBRERO', 'Febrero'),
        ('MARZO', 'Marzo'),
        ('ABRIL', 'Abril'),
        ('MAYO', 'Mayo'),
        ('JUNIO', 'Junio'),
        ('JULIO', 'Julio'),
        ('AGOSTO', 'Agosto'),
        ('SEPTIEMBRE', 'Septiembre'),
        ('OCTUBRE', 'Octubre'),
        ('NOVIEMBRE', 'Noviembre'),
        ('DICIEMBRE', 'Diciembre'),
    ]
    mes = models.CharField(max_length=20, choices=eleccion, default='ENERO')
    def __int__(self):
        return self.id