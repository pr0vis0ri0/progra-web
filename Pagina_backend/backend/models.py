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
    arriendo_propiedad = models.IntegerField()
    venta_propiedad = models.IntegerField()
    id_tipo_propiedad = models.ForeignKey(TipoPropiedad, null=True, on_delete=models.SET_NULL)

class CaracteristicasPropiedad (models.Model):
    dormitorios_propiedad = models.IntegerField()
    banos_propiedad = models.IntegerField()
    mascotas_propiedad = models.IntegerField()
    bodega_propiedad = models.IntegerField()
    estacionamiento = models.IntegerField()
    id_propiedad = models.ForeignKey(Propiedad,unique=True, null=True, on_delete=models.SET_NULL)

class Visita (models.Model):
    id_visita = models.AutoField(primary_key=True)
    dia_visita = models.TimeField()
    hora_visita = models.DateField()
    nombre_completo = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    correo = models.EmailField()
    telefono = models.CharField(max_length=11)

