from django.db import models


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=60, verbose_name='Nombre')
    Genero = models.CharField(max_length=60, verbose_name='Genero')
    Autor = models.CharField(max_length=60, verbose_name='Autor')
    Anio = models.CharField(max_length=60, verbose_name='Año')
    Tamanio = models.CharField(max_length=60, verbose_name='Tamaño')
    Prestamo = models.TextField(verbose_name='Prestamo', null= True)

def __str__(self):
    fila = "Nombre: " + self.Nombre + "-" + "Genero: " + self.Genero + "-" + "Autor: " + self.Autor + "-" + "Año: " + self.Anio + "-" + "Tamaño: " + self.Tamanio + "-" + "Prestamo: " + self.Prestamo
    return fila
