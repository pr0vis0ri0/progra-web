from django.contrib import admin
from .models import Region, Comuna, TipoPropiedad, Propiedad, CaracteristicasPropiedad, Visita
# Register your models here.

admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(TipoPropiedad)
admin.site.register(Propiedad)
admin.site.register(CaracteristicasPropiedad)
admin.site.register(Visita)