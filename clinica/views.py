from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic import View, DetailView,ListView
from .forms import CreateForm, CreateQuirofanoForm,UpdateClinicaForm
from .models import Clinica,Quirofano

class CrearClinicaView(CreateView):
    success_url = reverse_lazy('users:notificacion')
    template_name = 'clinica/registro_clinica.html'
    model = Clinica
    form_class = CreateForm


class ClinicasView(ListView):
    model = Clinica
    template_name = "clinica/consulta_clinica.html"
    context_object_name = "clinicas"


class UpdateClinicaView(UpdateView):

    model = Clinica
    template_name ='clinica/actualizar_clinica.html'
    success_url = reverse_lazy('users:clinicas')
    form_class = UpdateClinicaForm
