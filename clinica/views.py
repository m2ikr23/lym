from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic import View, DetailView,ListView
from .forms import CreateForm, CreateQuirofanoForm,UpdateClinicaForm,UpdateQuirofanoForm
from .models import Clinica,Quirofano

class CrearClinicaView(CreateView):
    success_url = reverse_lazy('users:notificacion')
    template_name = 'clinica/registro_clinica.html'
    model = Clinica
    form_class = CreateForm

class CrearQuirofanoView(CreateView):
    success_url = reverse_lazy('users:notificacion')
    template_name = 'clinica/incluir_quirofano.html'
    model = Quirofano
    form_class = CreateQuirofanoForm

class ClinicasView(ListView):
    model = Clinica
    template_name = "clinica/consulta_clinica.html"
    context_object_name = "clinicas"



class QuirofanosView(ListView):
    model = Quirofano
    template_name = "clinica/consultar_quirofano.html"
    context_object_name = "quirofanos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clinicas'] = Clinica.objects.all()
        return context


class UpdateClinicaView(UpdateView):

    model = Clinica
    template_name ='clinica/actualizar_clinica.html'
    success_url = reverse_lazy('users:clinicas')
    form_class = UpdateClinicaForm

class UpdateQuirofanoView(UpdateView):

    model = Quirofano
    template_name ='clinica/actualizar_quirofano.html'
    success_url = reverse_lazy('users:quirofanos')
    form_class = UpdateQuirofanoForm



def buscarQuiroView(request):
    clinica = Clinica.objects.get(id = request.GET['id'])
    quirofanos = Quirofano.objects.filter(clinica = clinica)
    data = serializers.serialize('json',quirofanos,
    fields = {'id','nombre','descripcion'})
    return HttpResponse(data,content_type='application/json')