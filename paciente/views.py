from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy 
from django.views.generic import View, DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required

from .forms import CreateForm
from .forms import SolicitarCitaForm
from .models import Paciente
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

def solicitarCitaView(request):
    form = SolicitarCitaForm
    return render(request,'paciente/solicitar_cita.html',{'form':form})
