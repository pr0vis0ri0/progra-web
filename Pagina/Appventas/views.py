from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html') 

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

def transbank(request):
    return render(request, 'transbank.html')