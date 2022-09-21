from django.db import models

# Create your models here.
class Directores(models.Model):
    nombre = models.TextField(max_length=200)

    def __str__(self):
        return self.nombre


class Peliculas(models.Model):
    nombre = models.TextField(max_length=200)    

    def __str__(self):
        return self.nombre