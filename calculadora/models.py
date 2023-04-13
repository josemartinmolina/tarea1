from django.db import models

# Create your models here.
class Reto(models.Model):
    nombre = models.CharField(max_length=30)
    minutos_jugados = models.IntegerField()

    def __str__(self):
        return f'{self.nombre},{self.minutos_jugados}'

class Jugadores(models.Model):
    grupo = models.CharField(max_length=2)
    num_lista = models.IntegerField()