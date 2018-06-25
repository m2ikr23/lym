from django.urls import path
from . import views
app_name = 'cirujano'
urlpatterns = [
    path('registro',views.CrearView.as_view(),name='registro'),
    path('planificar',views.planificarCirugiaView.as_view(),name="planificar"),
    path('updateCirugia/<str:pk>/',views.UpdateCirugiaView.as_view(),name='updateCirugia'),
    path('incluirCirugia',views.CrearCirugiaView.as_view(),name='incluirCirugia'),
    path('cirugias',views.CirugiasView.as_view(),name='cirugias'),
    path('updateEspecialidad/<str:pk>/',views.UpdateEspecialidadView.as_view(),name='updateEspcialidad'),
    path('incluirEspecialidad',views.CrearEspecialidadView.as_view(),name='incluirEspecialidad'),
    path('especialidades',views.EspecialidadView.as_view(),name='especialidades'),
    path('historia/list',views.HistoriasView.as_view(),name='historias'),
    path('historia/<int:pk>/actualizar/',views.UpdateHistoriaView.as_view(),name='updateHistoria'),
    path('historia/registrar/<int:pk>/',views.CrearHistoriaView.as_view(),name='registrarHistoria'),
]