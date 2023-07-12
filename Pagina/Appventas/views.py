from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def contacto(request):
    return render(request,'contacto.html')

def futuros_proyectos(request):
    return render(request,'futuros_proyectos.html')

def propiedades(request):
    return render(request,'propiedades.html')

def reg_propiedad(request):
    return render(request,'reg_propiedad.html')

def propiedad_caracteristicas(request, id_propiedad):
    return render(request, 'carac_propiedad.html' , {'id_propiedad' : id_propiedad})

def usuario(request):
    return render(request, 'usuario.html')

def administrador(request):
    return render(request, 'administrador.html')

def perfil(request):
    return render(request, 'perfil.html')

def preguntas_frecuentes(request):
    return render(request, 'preguntas_frecuentes.html')