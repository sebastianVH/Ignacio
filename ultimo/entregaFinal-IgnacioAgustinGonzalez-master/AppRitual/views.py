from django.shortcuts import render, redirect
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
def presentaciones(request):
    return render(request, "presentaciones.html")

# Reservaciones ---------------------------------------------------------------------------------------------------------------------------------------------------

@login_required()
def reservaciones(request):
    Reservaciones = ReservasMesa.objects.all()
    miReserva = reservacionFormularios()
    return render(request, "reservaciones.html", {"Reservaciones": Reservaciones, "miReserva": miReserva})

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
            return render(request, "reservaciones.html", {"miReserva": miReserva, "Reservaciones": Reservaciones})
    else:
        miReserva = reservacionFormularios()

    return render(request, "reservaciones.html", {"miReserva": miReserva, "Reservaciones": Reservaciones})

@login_required()
def buscarReservas(request):
    nombre = request.GET.get("nombre")
    apellido = request.GET.get("apellido")
    if nombre and apellido:
        reservas = ReservasMesa.objects.filter(nombre=nombre, apellido=apellido)
    elif nombre:
        reservas = ReservasMesa.objects.filter(nombre=nombre)
    elif apellido:
        reservas = ReservasMesa.objects.filter(apellido=apellido)
    return render(request, "getReservas.html", {"reservas": reservas})

@login_required()
def deleteReserva(request, id):
    reserva = ReservasMesa.objects.get(id=id)
    reserva.delete()
    return redirect('reservaciones')

@login_required
def editarReserva(request, id):
    reserva = ReservasMesa.objects.get(id=id) # TERMINARRRRRRRR


# Bodas y Eventos -----------------------------------------------------------------------------------------------------------------------------------------------------

@login_required()
def bodasEventos(request):
    Eventos = Evento.objects.all()
    miEvento = eventoFormularios()
    return render(request, "bodasEventos.html", {"Eventos": Eventos, "miEvento": miEvento})

@login_required()
def getBodasEventos(request):
    return render(request, "getBodasEventos.html")

@login_required()
def setBodasEventos(request):
    Eventos = Evento.objects.all()

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
            horaEvento = data["horaEvento"]
            numeroInvitados = data["numeroInvitados"]
            telefono = data["telefono"]
            email = data["email"]
            duracion = data["duracion"]
            costo = data["costo"]
            estado = data["estado"]
            anotaciones = data["anotaciones"]
            evento = Evento(nombre=nombre, apellido=apellido, tipoEvento=tipoEvento, privado=privado, fechaSolicitud=fechaSolicitud, fechaEvento=fechaEvento, horaEvento=horaEvento, numeroInvitados=numeroInvitados, telefono=telefono, email=email, duracion=duracion, costo=costo, estado=estado, anotaciones=anotaciones)
            evento.save()
            miEvento = eventoFormularios()
            return render(request, "bodasEventos.html", {"miEvento": miEvento, "Eventos": Eventos})
        else:
            print(miEvento.errors)
    miEvento = eventoFormularios()
    return render(request, "bodasEventos.html", {"miEvento": miEvento, "Eventos": Eventos})

@login_required()
def buscarBodasEventos(request):
    nombre = request.GET.get("nombre")
    apellido = request.GET.get("apellido")
    if nombre and apellido:
        eventos = Evento.objects.filter(nombre=nombre, apellido=apellido)
    elif nombre:
        eventos = Evento.objects.filter(nombre=nombre)
    elif apellido:
        eventos = Evento.objects.filter(apellido=apellido)
    return render(request, "getTrabajadores.html", {"eventos": eventos})


@login_required()
def deleteBodasEventos(request,id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect('bodasEventos')
    
@login_required
def editarBodasEventos(request,id):
    evento = Evento.objects.get(id=id)  # TERMINARRRRRRRR
    if request.method == "GET":
        form = eventoFormularios(instance=evento)
        return render(request,'editarBodasEventos.html',{"formulario":form,"id_evento":id})
    elif request.method == "POST":
        miEvento = eventoFormularios(request.POST)
        if miEvento.is_valid():
            data = miEvento.cleaned_data
            evento.nombre = data["nombre"]
            evento.apellido = data["apellido"]
            evento.tipoEvento = data["tipoEvento"]
            evento.privado = data["privado"]
            evento.fechaSolicitud = data["fechaSolicitud"]
            evento.fechaEvento = data["fechaEvento"]
            evento.horaEvento = data["horaEvento"]
            evento.numeroInvitados = data["numeroInvitados"]
            evento.telefono = data["telefono"]
            evento.email = data["email"]
            evento.duracion = data["duracion"]
            evento.costo = data["costo"]
            evento.estado = data["estado"]
            evento.anotaciones = data["anotaciones"]
            evento.save()
            return redirect('bodasEventos')
# Trabajadores --------------------------------------------------------------------------------------------------------------------------------------------------

@login_required()
def trabajadores(request):
    Trabajadores = Trabajadore.objects.all()
    miTrabajador = trabajadorFormularios()
    return render(request, "trabajadores.html", {"Trabajadores": Trabajadores, "miTrabajador": miTrabajador})

@login_required()
def getTrabajadores(request):
    return render(request, "getTrabajadores.html")

@login_required()
def setTrabajadores(request):
    Trabajadores = Trabajadore.objects.all()
    if request.method == 'POST':
        miTrabajador = trabajadorFormularios(request.POST, request.FILES)
        if miTrabajador.is_valid():
            data = miTrabajador.cleaned_data
            trabajador = Trabajadore(nombre=data["nombre"], apellido=data["apellido"], sector=data["sector"], telefono=data["telefono"], email=data["email"], fechaContratacion=data["fechaContratacion"], salario=data["salario"], foto_id=data["foto_id"], anotaciones=data["anotaciones"])
            trabajador.save()
            miTrabajador = trabajadorFormularios()
            return render(request, "trabajadores.html", {"miTrabajador": miTrabajador, "Trabajadores": Trabajadores})
    else:
        miTrabajador = trabajadorFormularios()

    return render(request, "trabajadores.html", {"miTrabajador": miTrabajador, "Trabajadores": Trabajadores})

@login_required()
def buscarTrabajadores(request):
    nombre = request.GET.get("nombre")
    apellido = request.GET.get("apellido")
    if nombre and apellido:
        trabajadores = Trabajadore.objects.filter(nombre=nombre, apellido=apellido)
    elif nombre:
        trabajadores = Trabajadore.objects.filter(nombre=nombre)
    elif apellido:
        trabajadores = Trabajadore.objects.filter(apellido=apellido)
    return render(request, "getTrabajadores.html", {"trabajadores": trabajadores})

@login_required()
def deleteTrabajadores(request, id):
    trabajadores = Trabajadore.objects.get(id=id)
    trabajadores.delete()
    return redirect('trabajadores')

@login_required
def editarTrabajadores(request, id):
    if request.method == "GET":
        trabajador = Trabajadore.objects.get(id=id) # TERMINARRRR
        form = trabajadorFormularios(instance=trabajador)
        return render(request,'editarTrabajadores.html',{"formulario":form,"trabajador":id})
    elif request.method == "POST":
        pass

# Login y Registro ---------------------------------------------------------------------------------------------------------------------------------------------------

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
            return redirect('login')
    else:
        return render(request, 'registro.html')

# Email ------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required()
def contactar(request): # Vista del mail
    return render(request, "contactar.html")

@login_required()
def contactarExitoso(request): # Vista del mail enviado
    return render(request, "contactarExitoso.html")

# Perfil ------------------------------------------------------------------------------------------------------------------------------------------------------------


@login_required()
def perfilVista(request):
    return render(request, 'perfil/perfil.html')


