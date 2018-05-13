from django.urls import path
from . import views
app_name = 'paciente'
urlpatterns = [
    path('registro',views.CrearView.as_view(),name='registro'),
    path('solicitar',views.solicitarCitaView ,name='solicitar'),
    
]