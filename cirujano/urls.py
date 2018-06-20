from django.urls import path
from . import views
app_name = 'cirujano'
urlpatterns = [
    path('registro',views.CrearView.as_view(),name='registro'),
    path('dashboard',views.DashboardView.as_view(),name="dashboard"),
    path('planificar',views.planificarCirugiaView.as_view(),name="planificar"),
    path('updateCirugia/<str:pk>/',views.UpdateCirugiaView.as_view(),name='updateCirugia'),
    path('incluirCirugia',views.CrearCirugiaView.as_view(),name='incluirCirugia'),
    path('cirugias',views.CirugiasView.as_view(),name='cirugias'),
    path('updateEspecialidad/<str:pk>/',views.UpdateEspecialidadView.as_view(),name='updateEspcialidad'),
    path('incluirEspecialidad',views.CrearEspecialidadView.as_view(),name='incluirEspecialidad'),
    path('especialidades',views.EspecialidadView.as_view(),name='especialidades'),
]