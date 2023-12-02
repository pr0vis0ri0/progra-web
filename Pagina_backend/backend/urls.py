from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('registro/', views.RegistroUsuario.as_view()),
    path('lista_propiedades/', views.PropiedadList.as_view()),
    path('arrendar_comprar_propiedad/', views.arrendarPropiedad, name='arrendar_propiedad'),
    path('propiedades_filtradas/', views.FiltroPropiedadDetail.as_view()),
    path('propiedades_pendientes/', views.PropiedadesPendientes.as_view()),
    path('adm_prop_pendientes/', views.AdminPropiedadesPendientes.as_view()),
    path('adm_prop_base/', views.AdminPropiedadesBase.as_view()),
    path('detalle_prop_adm/', views.DetallePropiedadAdmin.as_view()),
    path('propiedades_validadas/', views.PropiedadesValidadas.as_view()),
    path('registro_propiedad/', views.RegistroPropiedadDetail.as_view()),
    path('detalle_propiedad_pendiente/', views.PropiedadPendienteDetail.as_view()),
    path('detalle_propiedad_validada/', views.PropiedadValidadaDetail.as_view()),
    path('detalle_propiedad/<int:id_propiedad>', views.PropiedadDetail.as_view()),
    path('perfil_usuario/', views.PerfilUsuarioDetail.as_view()),
    path('transbank/create/', views.TransbankCreate.as_view()),
    path('transbank/commit/<str:tokenws>', views.TransbankCommit.as_view()),
]