from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ubicacion',views.ubicacion),
    path('contacto',views.contacto)
]