from django.urls import path
from . import views

urlpatterns = [
    path('', views.PacienteView, name='paciente'),
]