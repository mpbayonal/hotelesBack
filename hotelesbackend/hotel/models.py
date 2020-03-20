# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from polymorphic.models import PolymorphicModel
# Create your models here.

from django.contrib.auth.models import AbstractUser, UserManager

import datetime
from django.db import models


# Create your models here.
class Usuario(AbstractUser, PolymorphicModel):
    nombre = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=500)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    objects = UserManager()


class Hotel(Usuario):
    class Meta:
        verbose_name = 'hotel'
        verbose_name_plural = 'hoteles'

    def __str__(self):
        return self.nombre


class Cliente(Usuario):
    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.nombre


class Habitacion(models.Model):
    nombre = models.CharField(max_length=100)
    numeroCamasDobles = models.IntegerField()
    numeroCamasSencillas = models.IntegerField()
    costo = models.IntegerField()
    tipo = models.CharField(max_length=500)
    pHotel = models.ForeignKey(Hotel, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo


class Reserva(models.Model):
    fechaInicio = models.DateTimeField(default=datetime.datetime.utcnow)
    fechaFin = models.DateTimeField(default=datetime.datetime.utcnow)
    fechaReserva = models.DateTimeField(default=datetime.datetime.utcnow)
    pHotel = models.ForeignKey(Hotel, null=False, on_delete=models.CASCADE)
    pCliente = models.ForeignKey(Cliente, null=False, on_delete=models.CASCADE)
    pHabitacion = models.ManyToManyField( Habitacion)
    descripcion = models.CharField(max_length=500)
    pago = models.IntegerField()

    def __str__(self):
        return self.descripcion




class Servicio(models.Model):
    fueCumplida = models.IntegerField()
    descripcion = models.CharField(max_length=500)
    pHotel = models.ForeignKey(Hotel, null=False, on_delete=models.CASCADE)
    pReserva = models.ForeignKey(Reserva, null=False, on_delete=models.CASCADE)
    pHabitacion = models.ForeignKey(Habitacion, null=False, on_delete=models.CASCADE)
    pCliente = models.ForeignKey(Cliente, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
