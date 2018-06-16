from django.urls import path
from . import views
app_name = 'cirujano'
urlpatterns = [
    path('registro',views.CrearView.as_view(),name='registro'),
    path('dashboard',views.DashboardView.as_view(),name="dashboard"),
    path('planificar',views.planificarCirugiaView.as_view(),name="planificar"),
  
    
]