from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy 
from django.views.generic import View, DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreateForm,PlanificarForm
from .models import Cirujano,Cirugia_Planificada
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

