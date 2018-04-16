from django.shortcuts import render


def PacienteView(request):
    return render(request, 'paciente/paciente.html', {})
