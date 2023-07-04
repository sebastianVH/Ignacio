from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import reservacionFormularios, eventoFormularios, trabajadorFormularios
from .models import Trabajadore, Evento, ReservasMesa
from datetime import timezone

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
    Reservaciones = ReservasMesa.objects.all()
    return render(request, "reservaciones.html", {"Reservaciones": Reservaciones})

@login_required()
def presentaciones(request):
    return render(request, "presentaciones.html")

@login_required()
def bodasEventos(request):
    return render(request, "bodasEventos.html", {"miEvento": eventoFormularios()})

@login_required()
def trabajadores(request):
    Trabajadores = Trabajadore.objects.all()
    return render(request, "trabajadores.html", {"Trabajadores": Trabajadores})

@login_required()
def getReservas(request):
    return render(request, "getReservas.html")

@login_required()
def setReservas(request):
    Reservaciones = ReservasMesa.objects.all()

    if request.method == 'POST':
        miReserva = reservacionFormularios(request.POST)
        if miReserva.is_valid():
            data = miReserva.cleaned_data
            reserva = ReservasMesa(nombre=data["nombre"], apellido=data["apellido"], fechaSolicitud=data["fechaSolicitud"], fechaReserva=data["fechaReserva"], horaReserva=data["horaReserva"], numeroPersonas=data["numeroPersonas"], telefono=data["telefono"], email=data["email"], estado=data["estado"], anotaciones=data["anotaciones"])
            reserva.save()
            miReserva = reservacionFormularios()
            return render(request, "setReservas.html", {"miReserva": miReserva, "Reservaciones": Reservaciones})
    else:
        miReserva = reservacionFormularios()

    return render(request, "setReservas.html", {"miReserva": miReserva, "Reservaciones": Reservaciones})

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
            privado = data["privado"]
            fechaSolicitud = data["fechaSolicitud"]
            fechaEvento = data["fechaEvento"]
            numeroInvitados = data["numeroInvitados"]
            telefono = data["telefono"]
            email = data["email"]
            duracion = data["duracion"]
            costo = data["costo"]
            estado = data["estado"]
            anotaciones = data["anotaciones"]
            evento = Evento(nombre=nombre, apellido=apellido, tipoEvento=tipoEvento, privado=privado, fechaSolicitud=fechaSolicitud, fechaEvento=fechaEvento, numeroInvitados=numeroInvitados, telefono=telefono, email=email, duracion=duracion, costo=costo, estado=estado, anotaciones=anotaciones)
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
            return redirect("inicio")
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')


def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            userCreate.save()
            return redirect(request, 'login.html')
    else:
        return render(request, 'registro.html')


def contactar(request): # Vista del mail
    return render(request, "contactar.html")

def contactarExitoso(request): # Vista del mail enviado
    return render(request, "contactarExitoso.html")


def mostrar_reservas_vencidas(request):
    reservas_vencidas = ReservasMesa.objects.filter(fechaReserva__lt=timezone.now())
    now = timezone.now()
    if request.method == 'POST':
        reserva_id = request.POST.get('reserva_id')
        nueva_fecha_reserva = request.POST.get('nueva_fecha_reserva')
        reserva = ReservasMesa.objects.get(id=reserva_id)
        reserva.fechaReserva = nueva_fecha_reserva
        reserva.save()
        return redirect('getReservas')  # Redirigir a la vista de reservas

    return render(request, 'reservas_vencidas.html', {'reservas_vencidas': reservas_vencidas, 'now': now})

def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(ReservasMesa, id=reserva_id)

    if request.method == 'POST':
        form = reservacionFormularios(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('getReservas')  # Redirigir a la vista de reservas
    else:
        form = reservacionFormularios(instance=reserva)

    return render(request, 'editar_reserva.html', {'form': form})
