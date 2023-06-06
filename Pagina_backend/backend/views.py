from django.http import HttpResponse
from .serializers import RegionSerializer, ComunaSerializer, TipoPropiedadSerializer, PropiedadSerializer, CaracteristicasPropiedadSerializer, VisitaSerializer
from .models import *
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# dtl - Detalle
# srl - Serializer
class PropiedadList(APIView):
    def get(self, request):
        dtl_propiedad = Propiedad.objects.all()
        data_propiedades = []

        for propiedad in dtl_propiedad:
            dtl_caract = CaracteristicasPropiedad.objects.get(id_propiedad = propiedad.id_propiedad)
            srl_caract = CaracteristicasPropiedadSerializer(dtl_caract)

            dtl_comuna = Comuna.objects.get(pk = PropiedadSerializer(propiedad).data['id_comuna'])
            srl_comuna = ComunaSerializer(dtl_comuna)

            dtl_region = Region.objects.get(pk = srl_comuna.data['id_region'])
            srl_region = RegionSerializer(dtl_region)

            data_propiedad = {
                "data_propiedades" : PropiedadSerializer(propiedad).data,
                "data_caracteristicas" : srl_caract.data,
                "data_comunas" : srl_comuna.data,
                "data_regiones" : srl_region.data
            }
            data_propiedades.append(data_propiedad)
        
        return JSONResponse(data_propiedades)

class PropiedadDetail(APIView):
    def get(self, request, id_propiedad = None):
        if id_propiedad is not None :
            detalle_propiedad = Propiedad.objects.get(pk = id_propiedad)
            serializer_uno = PropiedadSerializer(detalle_propiedad)
            detalle_caracteristicas = CaracteristicasPropiedad.objects.get(id_propiedad = id_propiedad)
            serializer_dos = CaracteristicasPropiedadSerializer(detalle_caracteristicas)
            comuna_propiedad = Comuna.objects.get(pk = serializer_uno.data['id_comuna'])
            serializer_tres = ComunaSerializer(comuna_propiedad)
            region_propiedad = Region.objects.get(pk = serializer_tres.data['id_region'])
            serializer_cuatro = RegionSerializer(region_propiedad)
            serializer = {
                "data_propiedad" : serializer_uno.data,
                "data_caracteristica"  : serializer_dos.data,
                "data_comuna"  : serializer_tres.data,
                "data_region" : serializer_cuatro.data
            }
            return JSONResponse(serializer)