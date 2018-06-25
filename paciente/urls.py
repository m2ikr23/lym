from django.urls import path
from . import views
app_name = 'paciente'
urlpatterns = [
    path('registro',views.CrearView.as_view(),name='registro'),
    path('updatePaquete/<str:pk>/',views.UpdatePaqueteView.as_view(),name='updatePaquete'),
    path('incluirPaquete',views.CrearPaqueteView.as_view(),name='incluirPaquete'),
    path('paquetes',views.PaqueteView.as_view(),name='paquetes'),
    path('cita/<int:pk>/cancelar',views.DeleteCitaView.as_view(),name='cancelar'),
    path('paquetes/solicitar',views.SolicitarPaqueteView.as_view() ,name='solicitarPaquete'),
    path('solicitar/cita',views.CitaView.as_view() ,name='solicitar'),
    
]