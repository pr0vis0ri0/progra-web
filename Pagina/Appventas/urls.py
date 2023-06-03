from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.index),
    path('contacto', views.contacto),
    path('futuros_proyectos', views.futuros_proyectos),
    path('propiedades', views.propiedades),
    path('reg_propiedad', views.reg_propiedad)
]