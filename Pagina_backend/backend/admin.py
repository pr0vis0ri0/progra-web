from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *
# Register your models here.

# pip3 install django-import-export
# list_filster(); debe ser una tupla o una lista.
# list_display me imagino 

class RegionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_region',
                    'nombre_region')
    search_fields = ('id_region',
                     'nombre_region')

class ComunaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_comuna',
                    'nombre_comuna',
                    'id_region')
    search_display = ('id_comuna',
                      'nombre_comuna',
                      'id_region')

class TipoPropiedadAdmin (ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_tipo_propiedad',
                    'nombre_tipo_propiedad')
    search_display = ('id_tipo_propiedad',
                    'nombre_tipo_propiedad')

class PropiedadAdmin (ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_propiedad',
                    'valor_propiedad',
                    'es_arriendo',
                    'es_venta',
                    'id_tipo_propiedad')
    search_display = ('id_propiedad',
                    'valor_propiedad',
                    'es_arriendo',
                    'es_venta',
                    'id_tipo_propiedad')

class CaracteristicasPropiedadAdmin (ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cant_dormitorios',
                    'cant_banos',
                    'permite_mascotas',
                    'tiene_bodega',
                    'tiene_estacionamiento',
                    'id_propiedad')
    search_display = ('cant_dormitorios',
                    'cant_banos',
                    'permite_mascotas',
                    'tiene_bodega',
                    'tiene_estacionamiento',
                    'id_propiedad')
    
class VisitaAdmin (ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_visita',
                    'dia_visita',
                    'hora_visita',
                    'nombre_completo',
                    'rut',
                    'correo',
                    'telefono')
    search_display = ('id_visita',
                    'dia_visita',
                    'hora_visita',
                    'nombre_completo',
                    'rut',
                    'correo',
                    'telefono')
    
admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(TipoPropiedad, TipoPropiedadAdmin)
admin.site.register(Propiedad, PropiedadAdmin)
admin.site.register(CaracteristicasPropiedad, CaracteristicasPropiedadAdmin)
admin.site.register(Visita, VisitaAdmin)