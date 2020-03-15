from django.conf.urls import *
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.urls import include, path

from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [



    path('reserva/', views.ListReserva.as_view()),
    path('reserva/<int:pk>/', views.DetailReserva.as_view()),
    path('habitacion/', views.ListHabitacion.as_view()),
    path('habitacion/<int:pk>/', views.DetailHabitacion.as_view()),


    # url(r'^login/', views.login),
    # url(r'^&', views.index),

    # path('', views.index),

    # path('dashboard', views.dashboard),
    # path('logout', views.logout),

]