from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import reservacionFormularios, eventoFormularios, trabajadorFormularios
from .models import Trabajadore, Evento, ReservasMesa

@login_required()
def inicio(request):
    return render(request, "AppRitual/templatePadre.html")

@login_required()
def menu(request):
    return render(request, "menu.html")

@login_required()
def contacto(request):
    return render(request, "contacto.html")

@login_required()
def reservaciones(request):
    return render(request, "reservaciones.html", {"miReserva": reservacionFormularios()})

@login_required()
def presentaciones(request):
    return render(request, "presentaciones.html")

@login_required()
def bodasEventos(request):
    return render(request, "bodasEventos.html", {"miEvento": eventoFormularios()})

@login_required()
def trabajadores(request):
    return render(request, "trabajadores.html",  {"miTrabajador": trabajadorFormularios()})

@login_required()
def getReservas(request):
    return render(request, "getReservas.html")

@login_required()
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

@login_required()
def buscarReservas(request):
    nombre = request.GET.get("nombre")
    if nombre:
        reservas = ReservasMesa.objects.filter(nombre=nombre)
        return render(request, "getReservas.html", {"reservas": reservas})


@login_required()
def getBodasEventos(request):
    return render(request, "getBodasEventos.html")

@login_required()
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

@login_required()
def buscarBodasEventos(request):
    nombre = request.GET.get("nombre")
    if nombre:
        eventos = Evento.objects.filter(nombre__icontains=nombre)

    return render(request, "getBodasEventos.html", {"eventos": eventos})

@login_required()
def getTrabajadores(request):
    return render(request, "getTrabajadores.html")

@login_required()
def setTrabajadores(request):
    if request.method == 'POST':
        miTrabajador = trabajadorFormularios(request.POST, request.FILES)
        if miTrabajador.is_valid():
            data = miTrabajador.cleaned_data
            trabajador = Trabajadore(nombre=data["nombre"], apellido=data["apellido"], sector=data["sector"], telefono=data["telefono"], email=data["email"], fechaContratacion=data["fechaContratacion"], salario=data["salario"], foto_id=data["foto_id"], anotaciones=data["anotaciones"])
            trabajador.save()
            return render(request, "AppRitual/templatePadre.html")
    else:
        miTrabajador = trabajadorFormularios()

    return render(request, "setTrabajadores.html", {"miTrabajador": miTrabajador})

@login_required()
def buscarTrabajadores(request):
    nombre = request.GET.get("nombre")
    if nombre:
        trabajadores = Trabajadore.objects.filter(nombre=nombre)
        return render(request, "getTrabajadores.html", {"trabajadores": trabajadores})


def loginWeb(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['user'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, "AppRitual/templatePadre.html")
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')


def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            userCreate.save()
            return render(request, 'login.html')
    else:
        return render(request, 'registro.html')

