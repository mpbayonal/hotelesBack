from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'descripcion' ]

class ReservaSerializer(serializers.ModelSerializer):
    pHabitacion =  HabitacionSerializer(read_only=True, many=True)
    pCliente = ClienteSerializer(read_only=True)
    class Meta:
        model = Reserva
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'



