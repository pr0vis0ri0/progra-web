from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('inicio',views.index, name='inicio'),
    path('login', views.login, name='inicio_sesion'),
    path('contacto',views.contacto, name='contacto'),
    path('futuros_proyectos',views.futuros_proyectos, name='futuros_proyectos'),
    path('propiedades',views.propiedades, name='propiedades'),
    path('caracteristicas/<int:id_propiedad>', views.propiedad_caracteristicas, name= 'prop_carac'),
    path('reg_propiedad',views.reg_propiedad,name='reg_propiedad'),
    path('usuario', views.usuario),
    path('administrador', views.administrador),
    path('perfil', views.perfil, name = 'perfil_usuario'),
    path('preguntas_frecuentes', views.preguntas_frecuentes, name='preguntas_frecuentes')
]