from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('menu/', menu, name='menu'),
    path('reservaciones/', reservaciones, name='reservaciones'),
    path('contacto/', contacto, name='contacto'),
    path('trabajadores/', trabajadores, name='trabajadores'),
    path('presentaciones/', presentaciones, name='presentaciones'),
    path('bodasEventos/', bodasEventos, name='bodasEventos'),
    path('getReservas/', getReservas, name='getReservas'),
    path('setReservas/', setReservas, name='setReservas'),
    path('deleteReserva/<id>', deleteReserva, name='deleteReserva'),
    path('editarReserva/<id>', editarReserva, name='editarReserva'),
    path('buscarReservas/', buscarReservas, name='buscarReservas'),
    path('getBodasEventos/', getBodasEventos, name='getBodasEventos'),
    path('setBodasEventos/', setBodasEventos, name='setBodasEventos'),
    path('deleteBodasEventos/<id>', deleteBodasEventos, name='deleteBodasEventos'),
    path('editarBodasEventos/<id>', editarBodasEventos, name='editarBodasEventos'),
    path('buscarBodasEventos/', buscarBodasEventos, name='buscarBodasEventos'),
    path('getTrabajadores/', getTrabajadores, name='getTrabajadores'),
    path('setTrabajadores/', setTrabajadores, name='setTrabajadores'),
    path('buscarTrabajadores/', buscarTrabajadores, name='buscarTrabajadores'),
    path('deleteTrabajadores/<id>', deleteTrabajadores, name='deleteTrabajadores'),
    path('editarTrabajadores/<id>', editarTrabajadores, name='editarTrabajadores'),
    path('', loginWeb, name='login'),
    path('registro/', registro, name='registro'),
    path('', LogoutView.as_view(template_name="login.html"), name="logout"),
    path('contactar/', contactar, name='contactar'),
    path('contactarExitoso/', contactarExitoso, name='contactarExitoso'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
