from django.db import models

class Region (models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=30)

class Comuna (models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=30)
    id_region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)

class TipoPropiedad (models.Model):
    id_tipo_propiedad = models.AutoField(primary_key=True)
    nombre_tipo_propiedad = models.CharField(max_length=20)

class Propiedad (models.Model):
    id_propiedad = models.AutoField(primary_key=True)
    valor_propiedad = models.IntegerField()
    es_arriendo = models.IntegerField()
    es_venta = models.IntegerField()
    id_tipo_propiedad = models.ForeignKey(TipoPropiedad, null=True, on_delete=models.SET_NULL)

class CaracteristicasPropiedad (models.Model):
    cant_dormitorios = models.IntegerField()
    cant_banos = models.IntegerField()
    permite_mascotas = models.IntegerField()
    tiene_bodega = models.IntegerField()
    tiene_estacionamiento = models.IntegerField()
    id_propiedad = models.ForeignKey(Propiedad,unique=True, null=True, on_delete=models.SET_NULL)

class Visita (models.Model):
    id_visita = models.AutoField(primary_key=True)
    dia_visita = models.DateField()
    hora_visita = models.TimeField()
    nombre_completo = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    correo = models.EmailField()
    telefono = models.CharField(max_length=11)

