from django.db import models

# Create your models here.
class Carro(models.Model):
    marca = models.CharField(max_length=120)
    cantidad = models.IntegerField()
    pais = models.CharField(max_length=120)

    def __str__(self):
        return self.marca