"""Pagina_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from backend import viewsets
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from . import settings

# Creamos un router y registramos nuestro viewset

app_name = 'backend'

router = DefaultRouter()
router.register("region", viewsets.RegionViewSet, basename='Region')
router.register('comuna', viewsets.ComunaViewSet, basename='Comuna')
router.register('tipo_propiedad', viewsets.TipoPropiedadViewSet, basename='Tipo Propiedad')
router.register('propiedad', viewsets.PropiedadViewSet, basename='Propiedad')
router.register('caracteristicas_propiedad', viewsets.CaracteristicasPropiedadViewSet, basename='Características Propiedad')
router.register('visitas', viewsets.VisitaViewSet, basename='Visitas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/schema/', SpectacularAPIView.as_view(),name='schema'),
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]