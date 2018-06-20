from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic import View, DetailView,ListView
from .forms import CreateCirugiaForm,CreateEspecialidadForm,CreateForm,PlanificarForm,UpdateCirugiaForm,UpdateEspecialidadForm
from .models import Cirugia,Cirugia_Planificada,Cirujano,Especialidad
from users.views import DashboardView as Dash

class CrearView(CreateView):
    success_url = reverse_lazy('cirujano:registro')
    template_name = 'cirujano/registro_cirujano.html'
    model = Cirujano
    form_class = CreateForm

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.is_medical = True
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class DashboardView(Dash):
    
    def log(self):
        pass

class planificarCirugiaView(CreateView):
    success_url = reverse_lazy('cirujano:dashboard')
    template_name = 'cirujano/planificar.html'
    model = Cirugia_Planificada
    form_class = PlanificarForm

class CrearCirugiaView(CreateView):
    success_url = reverse_lazy('users:notificacion')
    template_name = 'cirujano/incluir_cirugia.html'
    model = Cirugia
    form_class = CreateCirugiaForm

class CrearEspecialidadView(CreateView):
    success_url = reverse_lazy('users:notificacion')
    template_name = 'cirujano/incluir_especialidad.html'
    model = Especialidad
    form_class = CreateEspecialidadForm

class UpdateCirugiaView(UpdateView):

    model = Cirugia
    template_name ='cirujano/actualizar_cirugia.html'
    success_url = reverse_lazy('users:cirugias')
    form_class = UpdateCirugiaForm

class UpdateEspecialidadView(UpdateView):

    model = Especialidad
    template_name ='cirujano/actualizar_especialidad.html'
    success_url = reverse_lazy('users:especialidades')
    form_class = UpdateEspecialidadForm

class CirugiasView(ListView):
    model = Cirugia
    template_name = "cirujano/consultar_cirugia.html"
    context_object_name = "cirugias"

class EspecialidadView(ListView):
    model = Especialidad
    template_name = "cirujano/consultar_especialidad.html"
    context_object_name = "especialidades"