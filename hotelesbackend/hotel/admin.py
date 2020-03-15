from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
admin.site.register(Reserva)
admin.site.register(Habitacion)

admin.site.register(Cliente)
admin.site.register(Hotel, UserAdmin)