from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'clinica'
urlpatterns = [
    path('registro',views.CrearClinicaView.as_view(),name='registro'),
    path('consultar',views.ClinicasView.as_view(),name='consultar'),
    path('quirofanos',views.QuirofanosView.as_view(),name='quirofanos'),
    path('update/<str:pk>/',views.UpdateClinicaView.as_view(),name='update'),
    path('updateQuiro/<str:pk>/',views.UpdateQuirofanoView.as_view(),name='updateQuiro'),
    path('incluir',views.CrearQuirofanoView.as_view(),name='incluir'),
    url('buscarQuiro/', views.buscarQuiroView , name="buscar" )
]  
    