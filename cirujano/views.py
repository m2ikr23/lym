from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic import View, DetailView,ListView
from .forms import CreateCirugiaForm,CreateEspecialidadForm,CreateForm,PlanificarForm,UpdateCirugiaForm,UpdateEspecialidadForm,CrearHistoriaForm,UpdateHistoriaForm,ConfirmarForm
from .models import Cirugia,Cirugia_Planificada,Cirujano,Especialidad,Historia,Cita
from clinica.models import Clinica, Quirofano

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

class planificarCirugiaView(CreateView):
    success_url = reverse_lazy('users:dashboard')
    template_name = 'cirujano/planificar.html'
    model = Cirugia_Planificada
    form_class = PlanificarForm
    fail_url = reverse_lazy('users:notificacionFailPlanificar')

    def form_valid(self,form):
        try:
            self.object = form.save(commit=False)
            self.object.paciente = Cita.objects.get(pk=self.kwargs['pk'])
            self.object.cirujano = Cirujano.objects.get(pk=self.request.user.pk)
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        except:
            return HttpResponseRedirect(self.fail_url)
    

    

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


class CrearHistoriaView(CreateView):
    success_url = reverse_lazy('users:notificacion')
    template_name = 'cirujano/registrar_historia.html'
    model = Historia
    form_class = CrearHistoriaForm
    fail_url = reverse_lazy('users:notificacionFailHistoria')


    def form_valid(self,form):
        try:
            self.object = form.save(commit=False)
            self.object.paciente = Cita.objects.get(pk=self.kwargs['pk'])
            self.object.medico = Cirujano.objects.get(pk=self.request.user.pk)
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        except:
            return HttpResponseRedirect(self.fail_url)
       

class HistoriasView(ListView):
    model = Historia
    template_name = "cirujano/consultar_historial.html"
    context_object_name = "historias"

class UpdateHistoriaView(UpdateView):

    model = Historia
    template_name ='cirujano/actualizar_historia.html'
    success_url = reverse_lazy('cirujano:historias')
    form_class = UpdateHistoriaForm

class ConfirmarView(UpdateView):

    model = Cita
    template_name ='cirujano/confirmar.html'
    success_url = reverse_lazy('users:dashboard')
    form_class = ConfirmarForm
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.confirmada = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
