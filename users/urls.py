from django.urls import path
from django.conf.urls import url
from . import views
app_name='users'
urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('create/',views.CrearView.as_view(),name='create'),
    path('update/',views.UpdateUserView.as_view(),name='update'),
    path('desactivate/<int:pk>/',views.DesactivateView.as_view(),name='desactivate'),
    path('activate/<int:pk>/',views.ActivateView.as_view(),name='activate'),
    path('delete/<int:pk>/',views.CirujanoDeleteView.as_view(),name='delete'),
    path('edit/',views.editFotoView.as_view() ,name='edit'),
    path('dashboard/',views.DashboardView.as_view(),name='dashboard'),
    path('dashboard/cirujanos',views.CirujanosView.as_view(),name='cirujanos'),
    path('show/<int:pk>/',views.ShowView.as_view(),name='show'),
    path('',views.homeView, name='home'),
    path('dashboard/clinicas',views.clinicaDashView, name='clinicas'),
    path('dashboard/quirofanos',views.quirofanoDashView, name='quirofanos'),
    path('dashboard/cirugias',views.cirugiaDashView, name='cirugias'),
    path('dashboard/especialidad',views.especialidadDashView, name='especialidades'),
    path('dashboard/paquetes',views.paqueteDashView, name='paquetes'),
    path('exito',views.notificacionView, name='notificacion'),
    path('info/',views.maxiView, name='Infomaxi'),
    path('infoplas/',views.plastiView, name='infoplasti'),
    path('infotraum/',views.traumaView, name='infotrauma'),
    path('infofta/',views.oftamoView, name='infoftamo'),
    path('infogene/',views.generalView, name='infogeneral'),
    path('infogineco/',views.gineView, name='infogine'),
    path('infootorri/',views.otorrinoView, name='infotorrino'),
    path('infouro/',views.uroloView, name='infourolo')
]