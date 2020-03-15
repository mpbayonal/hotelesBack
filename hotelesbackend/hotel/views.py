from django.shortcuts import render


from django.shortcuts import render

from .serializers import *
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
import os
from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

class ListReserva(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


# Create your views here.
class DetailReserva(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ListHabitacion(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = HabitacionSerializer


# Create your views here.
class DetailHabitacion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = HabitacionSerializer

@csrf_exempt
def send_reserva(request):

    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        hotel = Hotel.objects.get(id = data['hotel'])
        cliente = Cliente.objects.get(id=data['cliente'])

        #file_name = "{0}".format(input_image.name)
        nuevoReserva = Reserva(
            nombre=data['nombre'],
            apellido=data['apellido'],
            email=data['email'],
            estado=data['estado'],
            pago=data['pago'],
            hotel=hotel,
            cliente= cliente

        )
        nuevoReserva.save()

        serializer = ReservaSerializer(nuevoReserva, many=False)
        return JsonResponse(serializer.data, safe=False)
