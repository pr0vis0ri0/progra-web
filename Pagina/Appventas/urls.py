from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home),
    path('algo',views.algo)
]