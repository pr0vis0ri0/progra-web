from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html') 

def ubicacion(request):
    return render(request,'ubicacion.html') 

def contacto(request):
    return render(request,'contacto.html')

def futuros_proyectos(request):
    return render(request,'futuros_proyectos.html')

def departamentos(request):
    return render(request, 'departamentos.html')