from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('home',views.home),
    path('algo',views.algo)
=======
    path('inicio', views.index),
    path('local-de-venta', views.local_de_venta),
    path('contacto', views.contacto),
    path('futuros_proyectos', views.futuros_proyectos),
    path('departamentos', views.departamentos)
>>>>>>> main
]