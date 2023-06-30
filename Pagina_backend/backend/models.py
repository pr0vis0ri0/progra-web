from django.db import models
from django.contrib.auth.models import User

class Region (models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=70)
    capital_region = models.CharField(max_length=30, default='')
    
    def __str__ (self):
        return (str(self.id_region) + ' ' + self.nombre_region)
    
    class Meta :
        ordering = ['id_region']
    
class Comuna (models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=30)
    id_region = models.ForeignKey(Region, null = False , on_delete= models.DO_NOTHING)

    def __str__ (self):
        return (str(self.id_comuna) + ' ' + self.nombre_comuna)
    
    class Meta :
        ordering = ['id_comuna']

class TipoPropiedad (models.Model):
    id_tipo_propiedad = models.AutoField(primary_key=True)
    nombre_tipo_propiedad = models.CharField(max_length=20)

    def __str__(self):
        return (str(self.id_tipo_propiedad) + ' ' + self.nombre_tipo_propiedad)

    class Meta :
        ordering = ['id_tipo_propiedad']

class Propiedad (models.Model):
    id_propiedad = models.AutoField(primary_key=True)
    valor_propiedad = models.IntegerField()
    es_arriendo = models.BooleanField(default=0, null=False, blank=True)
    es_venta = models.BooleanField(default=0, null=False, blank=True)
    id_tipo_propiedad = models.ForeignKey(TipoPropiedad, null = False, on_delete = models.DO_NOTHING)
    id_comuna = models.ForeignKey(Comuna, null = False, on_delete = models.DO_NOTHING)
    esta_habilitado = models.BooleanField(default=0, null = False)

    def __str__(self):
        return str(self.id_propiedad)

    class Meta :
        ordering = ['id_propiedad']

class CaracteristicasPropiedad (models.Model):
    metros_totales = models.IntegerField(default=0)
    metros_utiles = models.IntegerField(default=0)
    cant_dormitorios = models.IntegerField()
    cant_banos = models.IntegerField()
    permite_mascotas = models.BooleanField(default=True, null=False)
    tiene_bodega = models.BooleanField(default=True, null=False)
    tiene_estacionamiento = models.BooleanField(default=True, null=False)
    id_propiedad = models.OneToOneField(Propiedad, null = False, on_delete = models.DO_NOTHING)

    class Meta :
        ordering = ['id_propiedad']

class Visita (models.Model):
    id_visita = models.AutoField(primary_key=True)
    dia_visita = models.DateField()
    hora_visita = models.TimeField()
    nombre_completo = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    correo = models.EmailField()
    telefono = models.CharField(max_length=11)
    id_propiedad = models.ForeignKey(Propiedad, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.id_visita

    class Meta :
        ordering = ['id_visita']

class Usuario (models.Model):
    id_usuario = models.AutoField(primary_key = True)
    primer_nombre = models.CharField(max_length= 50, default= "")
    segundo_nombre = models.CharField(max_length= 50, default= "")
    apellido_paterno = models.CharField(max_length= 50, default= "")
    apellido_materno = models.CharField(max_length= 50, default= "")
    email = models.EmailField(default= "")
    rut = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField(default= None)
    auth_user_id = models.ForeignKey(User, null = True, on_delete = models.DO_NOTHING)

    def __str__ (self):
        return str(self.rut)

    class Meta:
        ordering = ['id_usuario']
        db_table = 'MAESTRO_USUARIOS'

class Perfiles (models.Model):
    id_perfil = models.AutoField(primary_key= True)
    nombre_perfil = models.CharField(max_length= 75)

    def __str__ (self):
        return str(self.nombre_perfil)

    class Meta:
        ordering = ['id_perfil']
        db_table = 'MAESTRO_PERFILES'

class PerfilesUsuario (models.Model):
    id_registro = models.AutoField(primary_key=True) # Sólo por que Django te obliga XD
    id_usuario = models.ForeignKey(Usuario, null= False, on_delete= models.DO_NOTHING)
    id_perfil = models.ForeignKey(Perfiles, null = False, on_delete= models.DO_NOTHING)

    class Meta:
        ordering = ['id_usuario', 'id_perfil']
        db_table = 'MAESTRO_ASOC_USUARIO_PERFILES'