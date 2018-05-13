from django.urls import path
from django.conf.urls import url
from . import views
app_name='users'
urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('create/',views.CrearView.as_view(),name='create'),
    path('update/',views.UpdateUserView.as_view(),name='update'),
    path('edit/',views.editFotoView.as_view() ,name='edit'),
    path('dashboard/',views.DashboardView.as_view(),name='dashboard'),
    path('show/<int:pk>/',views.ShowView.as_view(),name='show'),
    path('',views.homeView, name='home')
]