from django.urls import path, include
from . import views

urlpatterns = [
    path('detalle_propiedad/', views.PropiedadList.as_view()),
    path('detalle_propiedad/<int:id_propiedad>', views.PropiedadDetail.as_view())
]