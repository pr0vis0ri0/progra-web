from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ubicacion(request):
    return render(request,'ubicacion.html') 