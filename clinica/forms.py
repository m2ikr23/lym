from django import forms
from .models import Clinica,Quirofano

class CreateForm(forms.ModelForm):

 class Meta:
        model = Clinica
        fields = ['id','nombre','direccion','telefono','email']
   
class CreateQuirofanoForm(forms.ModelForm):

 class Meta:
        model = Quirofano
        fields = ['clinica','nombre','descripcion']

class UpdateClinicaForm(forms.ModelForm):

    class Meta:

        model = Clinica
        fields = ['nombre','direccion','telefono','email']
   