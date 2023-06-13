from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

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
    id_propiedad = serializers.IntegerField()