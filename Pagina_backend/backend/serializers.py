from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class RegionSerializer (ModelSerializer):
    class Meta :
        model = Region
        fields = '__all__'

class ComunaSerializer (ModelSerializer):
    class Meta :
        model = Comuna
        fields = '__all__'

class TipoPropiedadSerializer (ModelSerializer):
    class Meta :
        model = TipoPropiedad
        fields = '__all__'

class PropiedadSerializer (ModelSerializer):
    class Meta :
        model = Propiedad
        fields = '__all__'

class CaracteristicasPropiedadSerializer (ModelSerializer):
    class Meta :
        model = CaracteristicasPropiedad
        fields = '__all__'

class VisitaSerializer (ModelSerializer):
    class Meta :
        model = Visita
        fields = '__all__'
        
class DetallePropiedadesSerializer (serializers.Serializer):
    id_propiedad = serializers.IntegerField()
    valor_propiedad = serializers.IntegerField()
    es_arriendo = serializers.BooleanField()
    es_venta = serializers.BooleanField()
    nombre_tipo_propiedad = serializers.CharField()
    nombre_comuna = serializers.CharField()
    nombre_region = serializers.CharField()

class ViewCaracteristicasSerializer (serializers.Serializer):
    id_propiedad = serializers.IntegerField()
    valor_propiedad = serializers.IntegerField()
    es_arriendo = serializers.BooleanField()
    es_venta = serializers.BooleanField()
    nombre_tipo_propiedad = serializers.CharField()
    metros_totales = serializers.IntegerField()
    metros_utiles = serializers.IntegerField()
    cant_dormitorios = serializers.IntegerField()
    cant_banos = serializers.IntegerField()
    permite_mascotas = serializers.BooleanField()
    tiene_bodega = serializers.BooleanField()
    tiene_estacionamiento = serializers.BooleanField()
    nombre_comuna = serializers.CharField()
    nombre_region = serializers.CharField()

class RegistroPropiedadSerializer (serializers.Serializer):
    id_usuario = serializers.IntegerField()
    valor_propiedad = serializers.IntegerField()
    es_arriendo = serializers.BooleanField()
    es_venta = serializers.BooleanField()
    id_tipo_propiedad = serializers.IntegerField()
    id_comuna = serializers.IntegerField()
    metros_totales = serializers.IntegerField()
    metros_utiles = serializers.IntegerField()
    cant_dormitorios = serializers.IntegerField()
    cant_banos = serializers.IntegerField()
    permite_mascotas = serializers.BooleanField()
    tiene_bodega = serializers.BooleanField()
    tiene_estacionamiento = serializers.BooleanField()

class RegistroUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class FiltroPropiedadSerializer(serializers.Serializer):
    id_comuna = serializers.IntegerField()
    valor_desde = serializers.IntegerField()
    valor_hasta = serializers.IntegerField()
    es_arriendo = serializers.BooleanField()
    es_venta = serializers.BooleanField()

class BasePropiedadesSerializer(serializers.Serializer):
    id_usuario = serializers.IntegerField()

class DetallePropiedadSerializer(serializers.Serializer):
    id_usuario = serializers.IntegerField()
    id_propiedad = serializers.IntegerField()

class TablasPropiedadesSerializer (serializers.Serializer):
    id_propiedad = serializers.IntegerField()
    valor_propiedad = serializers.IntegerField()
    es_arriendo = serializers.BooleanField()
    es_venta = serializers.BooleanField()
    nombre_tipo_propiedad = serializers.CharField()
    nombre_comuna = serializers.CharField()

class AdminPropiedadesSerializer (serializers.Serializer):
    id_propiedad = serializers.IntegerField()
    valor_propiedad = serializers.IntegerField()
    es_arriendo = serializers.BooleanField()
    es_venta = serializers.BooleanField()
    descripcion_estado = serializers.CharField()
    nombre_tipo_propiedad = serializers.CharField()
    metros_totales = serializers.IntegerField()
    metros_utiles = serializers.IntegerField()
    cant_dormitorios = serializers.IntegerField()
    cant_banos = serializers.IntegerField()
    permite_mascotas = serializers.BooleanField()
    tiene_bodega = serializers.BooleanField()
    tiene_estacionamiento = serializers.BooleanField()
    nombre_comuna = serializers.CharField()
    nombre_region = serializers.CharField()
    nombre_usuario = serializers.CharField()

class PutPropiedadSerializer (serializers.Serializer):
    id_usuario = serializers.IntegerField()
    id_propiedad = serializers.IntegerField()
    ultimo_estado = serializers.IntegerField()
    observacion_denegacion = serializers.CharField(allow_blank = True)