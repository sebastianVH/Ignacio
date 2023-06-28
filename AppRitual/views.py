from django.http import HttpResponse
from django.shortcuts import render
from .forms import reservacionFormularios, eventoFormularios, trabajadorFormularios
from .models import Trabajadore, Evento, ReservasMesa


def inicio(request):
    return render(request, "AppRitual/templatePadre.html")


def menu(request):
    return render(request, "menu.html")


def reservaciones(request):
    return render(request, "reservaciones.html", {"miReserva": reservacionFormularios()})


def galerias(request):
    return render(request, "galerias.html")


def ubicacion(request):
    return render(request, "ubicacion.html")


def contacto(request):
    return render(request, "contacto.html")


def especiales(request):
    return render(request, "especiales.html")


def bodasEventos(request):
    return render(request, "bodasEventos.html", {"miEvento": eventoFormularios()})


def trabajadores(request):
    return render(request, "trabajadores.html",  {"miTrabajador": trabajadorFormularios()})


def getReservas(request):
    return render(request, "getReservas.html")


def setReservas(request):
    if request.method == 'POST':
        miReserva = reservacionFormularios(request.POST)
        if miReserva.is_valid():
            data = miReserva.cleaned_data
            reserva = ReservasMesa(nombre=data["nombre"], apellido=data["apellido"], fechaSolicitud=data["fechaSolicitud"], fechaReserva=data["fechaReserva"], numeroPersonas=data["numeroPersonas"], telefono=data["telefono"], email=data["email"], costo=data["costo"], estado=data["estado"], anotaciones=data["anotaciones"])
            reserva.save()
            return render(request, "AppRitual/templatePadre.html")
    else:
        miReserva = reservacionFormularios()

    return render(request, "setReservas.html", {"miReserva": miReserva})


def buscarReservas(request):
    nombre = request.GET.get("nombre")
    if nombre:
        reservas = ReservasMesa.objects.filter(nombre=nombre)
        return render(request, "getReservas.html", {"reservas": reservas})
    else:
        respuesta = "No se enviaron datos"

    return HttpResponse(respuesta)


def getBodasEventos(request):
    return render(request, "bodasEventos.html")


def setBodasEventos(request):
    if request.method == 'POST':
        miEvento = eventoFormularios(request.POST)
        print(miEvento)
        if miEvento.is_valid():
            data = miEvento.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            tipoEvento = data["tipoEvento"]
            fechaSolicitud = data["fechaSolicitud"]
            fechaEvento = data["fechaEvento"]
            numeroInvitados = data["numeroInvitados"]
            telefono = data["telefono"]
            email = data["email"]
            duracion = data["duracion"]
            costo = data["costo"]
            estado = data["estado"]
            anotaciones = data["anotaciones"]
            evento = Evento(nombre=nombre, apellido=apellido, tipoEvento=tipoEvento, fechaSolicitud=fechaSolicitud, fechaEvento=fechaEvento,
                            numeroInvitados=numeroInvitados, telefono=telefono, email=email, duracion=duracion, costo=costo, estado=estado, anotaciones=anotaciones)
            evento.save()
            return render(request, "AppRitual/templatePadre.html")
        else:
            print(miEvento.errors)
    miEvento = eventoFormularios()
    return render(request, "bodasEventos.html", {"miEvento": miEvento})


def buscarBodasEventos(request):
    nombre = request.GET.get("nombre")
    if nombre:
        eventos = Evento.objects.filter(nombre__icontains=nombre)
    else:
        respuesta = "No se enviaron datos."
        return HttpResponse(respuesta)
    return render(request, "bodasEventos.html", {"eventos": eventos})


def getTrabajadores(request):
    return render(request, "getTrabajadores.html")


def setTrabajadores(request):
    if request.method == 'POST':
        miTrabajador = trabajadorFormularios(request.POST)
        if miTrabajador.is_valid():
            data = miTrabajador.cleaned_data
            trabajador = Trabajadore(nombre=data["nombre"], apellido=data["apellido"], sector=data["sector"],
                                     telefono=data["telefono"], email=data["email"], fechaContratacion=data["fechaContratacion"], salario=data["salario"], anotaciones=data["anotaciones"])
            trabajador.save()
            return render(request, "AppRitual/templatePadre.html")
    else:
        miTrabajador = trabajadorFormularios()

    return render(request, "setTrabajadores.html", {"miTrabajador": miTrabajador})


def buscarTrabajadores(request):
    nombre = request.GET.get("nombre")
    if nombre:
        trabajadores = Trabajadore.objects.filter(nombre=nombre)
        return render(request, "getTrabajadores.html", {"trabajadores": trabajadores})
    else:
        respuesta = "No se enviaron datos"

    return HttpResponse(respuesta)
