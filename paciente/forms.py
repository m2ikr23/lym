from django.forms import ModelForm
from django import forms
from .models import Paciente

class RegistroForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),min_length=8,max_length=20)
    email = forms.EmailField()

    class Meta:
        model = Paciente
        fields = ['first_name','last_name','email','password','address','phone','pais']
       

