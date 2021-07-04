from django.db import models

# Create your models here.


class AbdominalsData(models.Model):
    hourstart = models.TimeField(null=False, verbose_name='Hora de Inicio')
    hourend = models.TimeField(null=False, verbose_name='Hora de Fin')
    date = models.DateField(null=False, verbose_name='Fecha')
    nabs = models.IntegerField(null=False, default=0, verbose_name='Cantidad de Abdominales')


class WalkingData(models.Model):
    hourstart = models.TimeField(null=False, verbose_name='Hora de Inicio')
    hourend = models.TimeField(null=False, verbose_name='Hora de Fin')
    date = models.DateField(null=False, verbose_name='Fecha')
    nabs = models.IntegerField(null=False, default=0, verbose_name='Cantidad de Pasos')