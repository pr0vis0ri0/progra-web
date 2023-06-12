from django.http import HttpResponse
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.db import connection

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class PropiedadDetail(APIView):
    def get(self, request, id_propiedad = None):
        if id_propiedad is not None :
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM vista_caracteristicas_propiedades WHERE id_propiedad = %s', [id_propiedad])
                result = cursor.fetchone()

            if result is not None:
                nombres_columnas = [desc[0] for desc in cursor.description]
                data = dict(zip(nombres_columnas, result))
                return JSONResponse(data)
            else :
                return JSONResponse(status.HTTP_404_NOT_FOUND)
            
class PropiedadList(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM vista_detalle_propiedades')
            resultados = cursor.fetchall()
        data = []

        if resultados is not None :
            for fila in resultados:
                nombres_columnas = [desc[0] for desc in cursor.description]
                item = dict(zip(nombres_columnas, fila))
                data.append(item)

            return JSONResponse(data)
        else :
            return JSONResponse(status.HTTP_404_NOT_FOUND)