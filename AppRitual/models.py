from django.db import models
from django.core.validators import MaxValueValidator

class Trabajadore(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    sector = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")
    email = models.EmailField()
    fechaContratacion = models.DateField(verbose_name="Fecha Contratación")
    salario = models.IntegerField()
    foto_id = models.ImageField(upload_to='fotos_id', blank=True) # Campo no obligatorio para agilizar el proceso, ya que es una app de prueba. (La foto todavía no se visualiza)
    anotaciones = models.TextField(blank=True, verbose_name="Anotaciones (opcionales)")

    def __str__(self):
        return f'{self.nombre} {self.apellido} | {self.sector} | {self.telefono} | {self.email} | Fecha Contratación: {self.fechaContratacion} | Salario: {self.salario} '

class ReservasMesa(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechaSolicitud = models.DateField(verbose_name="Fecha Solicitud")
    fechaReserva = models.DateTimeField(verbose_name="Fecha Reserva")
    horaReserva = models.TimeField(verbose_name="Hora Reserva")
    numeroPersonas = models.IntegerField(verbose_name="Número Personas")
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")
    email = models.EmailField(blank=True, null=True, verbose_name="Email (opcional)")
    costo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name="Costo (opcional)")
    estado = models.BooleanField(verbose_name="Estado: (activo ✔ / inactivo ✘)")
    anotaciones = models.TextField(blank=True, verbose_name="Anotaciones (Opcional)")

    def __str__(self):
        return f'{self.nombre} {self.apellido} | Fecha Solicitud: {self.fechaSolicitud} | Fecha Reserva: {self.fechaReserva} {self.horaReserva} | Número Personas: {self.numeroPersonas} | {self.telefono} | {self.estado} | '


class Evento(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    tipoEvento = models.CharField(max_length=40, verbose_name="Tipo Evento")
    privado = models.BooleanField(verbose_name="Evento Privado (privado ✔ / semiprivado ✘)")
    fechaSolicitud = models.DateTimeField(verbose_name="Fecha Solicitud")
    fechaEvento = models.DateTimeField(verbose_name="Fecha Evento")
    numeroInvitados = models.IntegerField(verbose_name="Número Invitados (máx 115)",
        validators=[MaxValueValidator(115)])   # Se importa MaxValueValidator para establecer como tope máximo de invitados.
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")
    email = models.EmailField(blank=True, null=True, verbose_name="Email (opcional)")
    duracion = models.DurationField(verbose_name="Duración (horas)")
    costo = models.IntegerField(blank=True, verbose_name="Costo: (opcional)")
    estado = models.BooleanField(verbose_name="Estado (activo ✔ / inactivo ✘)")
    anotaciones = models.TextField(blank=True, verbose_name="Anotaciones (opcional)")

    def __str__(self):
        return f'{self.nombre} {self.apellido} | Tipo: {self.tipoEvento} | Fecha Solicitud: {self.fechaSolicitud} | Fecha Evento: {self.fechaEvento} | Cant. Invitados: {self.numeroInvitados} | {self.telefono} | {self.estado} | Duración: {self.duracion} | Costo: ${self.costo}'

