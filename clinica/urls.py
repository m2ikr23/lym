from django.urls import path
from . import views
app_name = 'clinica'
urlpatterns = [
    path('registro',views.CrearClinicaView.as_view(),name='registro'),
    path('consultar',views.ClinicasView.as_view(),name='consultar'),
    path('update/<str:pk>/',views.UpdateClinicaView.as_view(),name='update'),
]  
    