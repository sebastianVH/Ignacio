from django.contrib import admin
from .models import Trabajadore, ReservasMesa, Evento

class TrabajadoreAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "sector", "telefono", "email", "fechaContratacion", "salario")
    list_filter = ("nombre", "apellido", "sector", "telefono", "email", "fechaContratacion", "salario")
    search_fields = ("nombre", "apellido", "sector", "telefono", "email", "fechaContratacion", "salario")


class ReservasMesaAdmin(admin.ModelAdmin):
    list_filter = ("nombre", "apellido", "fechaSolicitud", "fechaReserva", "telefono", "email", "costo", "estado")
    list_display = ("nombre", "apellido", "fechaSolicitud", "fechaReserva", "telefono", "email", "costo", "estado")
    search_fields = ("nombre", "apellido", "fechaSolicitud", "fechaReserva", "telefono", "email", "costo", "estado")
    date_hierarchy = "fechaReserva"


class EventoAdmin(admin.ModelAdmin):
    list_filter = ("nombre", "apellido", "tipoEvento", "fechaSolicitud", "fechaEvento", "telefono", "email", "costo", "estado")
    list_display = ("nombre", "apellido", "tipoEvento", "fechaSolicitud", "fechaEvento", "telefono", "email", "costo", "estado")
    search_fields = ("nombre", "apellido", "tipoEvento", "fechaSolicitud", "fechaEvento", "telefono", "email", "costo", "estado")
    date_hierarchy = "fechaEvento"

class MenuBebidasAdmin(admin.ModelAdmin):
    list_display = "nombre"

class MenuComidaAdmin(admin.ModelAdmin):
    list_display = "nombre"


admin.site.register(Trabajadore, TrabajadoreAdmin)
admin.site.register(ReservasMesa, ReservasMesaAdmin)
admin.site.register(Evento, EventoAdmin)
