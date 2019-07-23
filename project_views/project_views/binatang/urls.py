from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.daftar_binatang),
    path('db/', views.db_binatang),
    path('form/', views.input_Hewan)
]
