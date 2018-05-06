from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import RegistroForm

# Create your views here.

class PacienteView(View):
    form_paciente = RegistroForm
    template_name = 'paciente/registroPaciente.html'
    initial = {'key':'value'}
    def get(self,request,*args,**kwargs):
        form=self.form_paciente(initial = self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = self.form_paciente(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request,self.template_name,{'form':form})
