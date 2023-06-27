# Generated by Django 4.0 on 2023-06-27 03:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('tipoEvento', models.CharField(max_length=40, verbose_name='Tipo Evento')),
                ('fechaSolicitud', models.DateTimeField(verbose_name='Fecha Solicitud')),
                ('fechaEvento', models.DateTimeField(verbose_name='Fecha Evento')),
                ('numeroInvitados', models.IntegerField(validators=[django.core.validators.MaxValueValidator(115)], verbose_name='Número Invitados (máx 115)')),
                ('telefono', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email (opcional)')),
                ('duracion', models.DurationField(verbose_name='Duración(horas)')),
                ('costo', models.IntegerField(blank=True, verbose_name='Costo: (opcional)')),
                ('estado', models.BooleanField(verbose_name='Estado (activo ✔ / inactivo ✘)')),
                ('anotaciones', models.TextField(blank=True, verbose_name='Anotaciones(opcionales)')),
            ],
        ),
        migrations.CreateModel(
            name='ReservasMesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('fechaSolicitud', models.DateTimeField(verbose_name='Fecha Solicitud')),
                ('fechaReserva', models.DateTimeField(verbose_name='Fecha Reserva')),
                ('numeroPersonas', models.IntegerField(verbose_name='Número Personas')),
                ('telefono', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email (opcional)')),
                ('costo', models.IntegerField(blank=True, verbose_name='Costo: (opcional)')),
                ('estado', models.BooleanField(verbose_name='Estado: (activo ✔ / inactivo ✘)')),
                ('anotaciones', models.TextField(blank=True, verbose_name='Anotaciones(Opcional)')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajadore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('sector', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=254)),
                ('fechaContratacion', models.DateField(verbose_name='Fecha Contratación')),
                ('salario', models.IntegerField()),
                ('foto_id', models.ImageField(blank=True, upload_to='fotos_id/')),
                ('anotaciones', models.TextField(blank=True, verbose_name='Anotaciones(opcionales)')),
            ],
        ),
    ]
