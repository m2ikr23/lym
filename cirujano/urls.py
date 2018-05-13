from django.urls import path
from . import views
app_name = 'cirujano'
urlpatterns = [
    path('registro',views.CrearView.as_view(),name='registro'),
  
    
]