from django.urls import path
from .views import PacienteView
urlpatterns = [
    path('',PacienteView.as_view(),name='registro')
]