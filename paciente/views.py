from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy 
from django.views.generic import View, DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic import View, DetailView,ListView
from .forms import CreateForm,CreatePaqueteForm,UpdatePaqueteForm
from .forms import SolicitarCitaForm
from .models import Paciente,Paquete
from cirujano.models import Cita
from users.models import Country
# Create your views here.


class CrearView(CreateView):
    success_url = reverse_lazy('users:notificacion')
    template_name = 'paciente/registro_paciente.html'
    model = Paciente
    form_class = CreateForm

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.is_pacient = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class CrearPaqueteView(CreateView):
    success_url = reverse_lazy('users:notificacion')
    template_name = 'paciente/incluir_paquete.html'
    model = Paquete
    form_class = CreatePaqueteForm

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class UpdatePaqueteView(UpdateView):

    model = Paquete
    template_name ='paciente/actualizar_paquete.html'
    success_url = reverse_lazy('users:paquetes')
    form_class = UpdatePaqueteForm


class PaqueteView(ListView):
    model = Paquete
    template_name = "paciente/consultar_paquete.html"
    context_object_name = "paquetes"



class CitaView(CreateView):
    success_url = reverse_lazy('users:notificacion')
    template_name = 'paciente/solicitar_cita.html'
    model = Cita
    form_class = SolicitarCitaForm

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.paciente = Paciente.objects.get(pk=self.request.user.pk)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
     
class CitaDetailView(DetailView):
    model = Cita
    template_name = "paciente/consultar_cita.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['citas'] = Cita.objects.get(paciente=self.request.user)
        return context
     
    

