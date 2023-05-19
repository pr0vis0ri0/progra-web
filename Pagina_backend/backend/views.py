from django.http import HttpResponse
from .serializers import RegionSerializer, ComunaSerializer, TipoPropiedadSerializer, PropiedadSerializer, CaracteristicasPropiedadSerializer, VisitaSerializer
from .models import *
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class RegionList(APIView):
    def get(self, request, format=None):
         registro = Region.objects.all()
         serializer = RegionSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = RegionSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=status.HTTP_201_CREATED)
        return JSONResponse(registro.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegionDetail(APIView):
    def get(self,request,id_region = None):
        if id_region is not None :
            registro = Region.objects.get(pk = id_region)
            serializer = RegionSerializer(registro)
            return JSONResponse(serializer.data)

    def put(self, request, id_region, format=None):
        registro = Region.objects.get(pk = id_region)
        serializer = RegionSerializer(registro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = status.HTTP_200_OK)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id_region, format=None):
        registro = Region.objects.get(pk = id_region)
        serializer = RegionSerializer(registro, data=request.data)
        if serializer.is_valid():
            registro.delete()
            return JSONResponse(serializer.data, status = status.HTTP_200_OK)
        return JSONResponse(serializer.errors,status=status.HTTP_204_NO_CONTENT)
    
class ComunaList(APIView):
    def get(self, request, format=None):
         registro = Comuna.objects.all()
         serializer = ComunaSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = ComunaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=status.HTTP_201_CREATED)
        return JSONResponse(registro.errors, status=status.HTTP_400_BAD_REQUEST)

class ComunaDetail(APIView):
    def get(self,request,id_comuna = None):
        if id_comuna is not None :
            registro = Comuna.objects.get(pk = id_comuna)
            serializer = ComunaSerializer(registro)
            return JSONResponse(serializer.data)

    def put(self, request, id_comuna, format=None):
        registro = Comuna.objects.get(pk = id_comuna)
        serializer = ComunaSerializer(registro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = status.HTTP_200_OK)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id_comuna, format=None):
        registro = Comuna.objects.get(pk = id_comuna)
        serializer = ComunaSerializer(registro, data=request.data)
        if serializer.is_valid():
            registro.delete()
            return JSONResponse(serializer.data, status = status.HTTP_200_OK)
        return JSONResponse(serializer.errors,status=status.HTTP_204_NO_CONTENT)

class TipoPropiedadList(APIView):
    def get(self, request, format=None):
         registro = TipoPropiedad.objects.all()
         serializer = TipoPropiedadSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = TipoPropiedadSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=status.HTTP_201_CREATED)
        return JSONResponse(registro.errors, status=status.HTTP_400_BAD_REQUEST)

class TipoPropiedadDetail(APIView):
    def get(self,request,id_tipo_propiedad = None):
        if id_tipo_propiedad is not None :
            registro = TipoPropiedad.objects.get(pk = id_tipo_propiedad)
            serializer = TipoPropiedadSerializer(registro)
            return JSONResponse(serializer.data)

    def put(self, request, id_tipo_propiedad, format=None):
        registro = TipoPropiedad.objects.get(pk = id_tipo_propiedad)
        serializer = TipoPropiedadSerializer(registro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = status.HTTP_200_OK)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id_tipo_propiedad, format=None):
        registro = TipoPropiedad.objects.get(pk = id_tipo_propiedad)
        serializer = TipoPropiedadSerializer(registro, data=request.data)
        if serializer.is_valid():
            registro.delete()
            return JSONResponse(serializer.data, status = status.HTTP_200_OK)
        return JSONResponse(serializer.errors,status=status.HTTP_204_NO_CONTENT)
    
class PropiedadList(APIView):
    def get(self, request, format=None):
         registro = Propiedad.objects.all()
         serializer = PropiedadSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = PropiedadSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=status.HTTP_201_CREATED)
        return JSONResponse(registro.errors, status=status.HTTP_400_BAD_REQUEST)

class PropiedadDetail(APIView):
    def get(self,request,id_propiedad = None):
        if id_propiedad is not None :
            registro = Propiedad.objects.get(pk = id_propiedad)
            serializer = PropiedadSerializer(registro)
            return JSONResponse(serializer.data)

    def put(self, request, id_propiedad, format=None):
        registro = Propiedad.objects.get(pk = id_propiedad)
        serializer = PropiedadSerializer(registro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = status.HTTP_200_OK)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id_propiedad, format=None):
        registro = Propiedad.objects.get(pk = id_propiedad)
        serializer = PropiedadSerializer(registro, data=request.data)
        if serializer.is_valid():
            registro.delete()
            return JSONResponse(serializer.data, status = status.HTTP_200_OK)
        return JSONResponse(serializer.errors,status=status.HTTP_204_NO_CONTENT)

class CaracteristicasPropiedadList(APIView):
    def get(self, request, format=None):
         registro = CaracteristicasPropiedad.objects.all()
         serializer = CaracteristicasPropiedadSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = CaracteristicasPropiedadSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=status.HTTP_201_CREATED)
        return JSONResponse(registro.errors, status=status.HTTP_400_BAD_REQUEST)

class CaracteristicasPropiedadDetail(APIView):
    def get(self,request,id_propiedad = None):
        if id_propiedad is not None :
            registro = CaracteristicasPropiedad.objects.filter(id_propiedad = id_propiedad)
            serializer = CaracteristicasPropiedadSerializer(registro)
            return JSONResponse(serializer.data)

    def put(self, request, id_propiedad, format=None):
        registro = CaracteristicasPropiedad.objects.filter(id_propiedad = id_propiedad)
        serializer = CaracteristicasPropiedadSerializer(registro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = status.HTTP_200_OK)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id_propiedad, format=None):
        registro = CaracteristicasPropiedad.objects.filter(id_propiedad = id_propiedad)
        serializer = CaracteristicasPropiedadSerializer(registro, data=request.data)
        if serializer.is_valid():
            registro.delete()
            return JSONResponse(serializer.data, status = status.HTTP_200_OK)
        return JSONResponse(serializer.errors,status=status.HTTP_204_NO_CONTENT)

class VisitaList(APIView):
    def get(self, request, format=None):
         registro = Visita.objects.all()
         serializer = VisitaSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = VisitaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=status.HTTP_201_CREATED)
        return JSONResponse(registro.errors, status=status.HTTP_400_BAD_REQUEST)

class VisitaDetail(APIView):
    def get(self,request,id_visita = None):
        if id_visita is not None :
            registro = Visita.objects.get(pk = id_visita)
            serializer = VisitaSerializer(registro)
            return JSONResponse(serializer.data)

    def put(self, request, id_visita, format=None):
        registro = Visita.objects.get(pk = id_visita)
        serializer = VisitaSerializer(registro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = status.HTTP_200_OK)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id_visita, format=None):
        registro = Visita.objects.get(pk = id_visita)
        serializer = VisitaSerializer(registro, data=request.data)
        if serializer.is_valid():
            registro.delete()
            return JSONResponse(serializer.data, status = status.HTTP_200_OK)
        return JSONResponse(serializer.errors,status=status.HTTP_204_NO_CONTENT)