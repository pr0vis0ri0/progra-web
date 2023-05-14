from django.urls import path
from . import views


urlpatterns = [
    path('region/', views.RegionList.as_view()),
    path('region/<int:id_region>', views.RegionDetail.as_view()),

    path('comuna/', views.ComunaList.as_view()),
    path('comuna/<int:id_comuna>', views.ComunaDetail.as_view()),

    path('tipo_propiedad/', views.TipoPropiedadList.as_view()),
    path('tipo_propiedad/<int:id_tipo_propiedadn>', views.TipoPropiedadDetail.as_view()),

    path('propiedad/', views.PropiedadList.as_view()),
    path('propiedad/<int:id_propiedad>', views.PropiedadList.as_view()),

    path('car_propiedad/', views.CaracteristicasPropiedadList.as_view()),
    path('car_propiedad/<int:id_propiedad>', views.CaracteristicasPropiedadDetail.as_view()),

    path('visita/', views.VisitaList.as_view()),
    path('visita/<int:id_visita>', views.VisitaDetail.as_view())
]