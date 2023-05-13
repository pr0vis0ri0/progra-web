from django.shortcuts import render
from django.http import HttpResponse
from .serializers import RegionSerializer, ComunaSerializer, TipoPropiedadSerializer, PropiedadSerializer, CaracteristicasPropiedadSerializer, VisitaSerializer
from .models import *
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
##from django.http import JSONResponse
from rest_framework.renderers import JSONRenderer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def RegionSerializer(request):
    region = Region.objects.all()
    serializer = RegionSerializer(region, many = True)
    return JSONResponse(serializer.data)

def ComunaSerializer(request):
    comuna = Comuna.objects.all()
    serializer = ComunaSerializer(comuna, many = True)
    return JSONResponse(serializer.data)

def TipoPropiedadSerializer(request):
    tipopropiedad = TipoPropiedad.objects.all()
    serializer = TipoPropiedad(tipopropiedad, many = True)
    return JSONResponse(serializer.data)

def PropiedadSerializer(request):
    propiedad = Propiedad.objects.all()
    serializer = PropiedadSerializer(propiedad, many = True)
    return JSONResponse(serializer.data)

def CaracteristicasPropiedadSerializer(request):
    caracteristicaspropiedad = CaracteristicasPropiedad.objects.all()
    serializer = CaracteristicasPropiedad(caracteristicaspropiedad, many = True)
    return JSONResponse(serializer.data)

def VisitaSerializer(request):
    visita = Visita.objects.all()
    serializer = RegionSerializer(visita, many = True)
    return JSONResponse(serializer.data)

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def rf_region(request):
    if request.method == 'GET':
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True) 
        return JSONResponse(serializer.data)
    elif request.method == 'POST': 
        data = JSONParser().parse(request)
        region = RegionSerializer(data=data)
        if Region.is_valid():
            Region.save()
            return JSONResponse(region.data, status=201)
    return JSONResponse(region.errors, status=410)