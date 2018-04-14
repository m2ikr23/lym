from django.shortcuts import render,redirect
from .froms import RegistroP
from .models import Paciente
def registroPView(request):

    if request.method == "POST":
        form= RegistroP(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.status = 'a'
            paciente.save()
            return redirect('home')
    else:
        form = RegistroP()

    return render(request,'users/registroPaciente.html',{'form':form})
    