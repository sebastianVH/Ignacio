from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='inicio'),
    path('menu/', menu, name='menu'),
    path('reservaciones/', reservaciones, name='reservaciones'),
    path('contacto/', contacto, name='contacto'),
    path('trabajadores/', trabajadores, name='trabajadores'),
    path('presentaciones/', presentaciones, name='presentaciones'),
    path('bodasEventos/', bodasEventos, name='bodasEventos'),
    path('getReservas/', getReservas, name='getReservas'),
    path('setReservas/', setReservas, name='setReservas'),
    path('buscarReservas/', buscarReservas, name='buscarReservas'),
    path('getBodasEventos/', getBodasEventos, name='getBodasEventos'),
    path('setBodasEventos/', setBodasEventos, name='setBodasEventos'),
    path('buscarBodasEventos/', buscarBodasEventos, name='buscarBodasEventos'),
    path('getTrabajadores/', getTrabajadores, name='getTrabajadores'),
    path('setTrabajadores/', setTrabajadores, name='setTrabajadores'),
    path('buscarTrabajadores/', buscarTrabajadores, name='buscarTrabajadores'),
    path('login/', loginWeb, name='login'),
    path('registro/', registro, name='registro'),
    path('logout/', LogoutView.as_view(template_name="login.html"), name="logout"),

]
