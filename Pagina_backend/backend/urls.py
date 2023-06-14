from django.urls import path, include
from . import views

urlpatterns = [
    path('registro/', views.RegistroUsuarioDetail.as_view()),
    path('lista_propiedades/', views.PropiedadList.as_view()),
    path('registro_propiedad/', views.RegistroPropiedadDetail.as_view()),
    path('detalle_propiedad/<int:id_propiedad>', views.PropiedadDetail.as_view())
]