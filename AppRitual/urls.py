from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('menu/', menu, name='menu'),
    path('reservaciones/', reservaciones, name='reservaciones'),
    path('galerias/', galerias, name='galerias'),
    path('ubicacion/', ubicacion, name='ubicacion'),
    path('contacto/', contacto, name='contacto'),
    path('trabajadores/', trabajadores, name='trabajadores'),
    path('especiales/', especiales, name='especiales'),
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

]
