from django.forms import ModelForm
from django import forms
from .models import Paciente

class CreateForm(forms.ModelForm):
    email = forms.EmailField( widget = forms.EmailInput)
    password = forms.CharField(max_length=20,min_length=8,widget=forms.PasswordInput())
    repeat_password = forms.CharField(max_length=20,min_length=8,widget=forms.PasswordInput())
    birthdate = forms.CharField(widget=forms.DateTimeInput())
   
    class Meta:
        model = Paciente
        fields = ['first_name','last_name','dni','birthdate','pais','address',
                    'email','password']

    def clean_repeat_password(self):
        value_pass = self.cleaned_data['password']
        value_pass2 = self.cleaned_data['repeat_password']
        if value_pass2 != value_pass:
            raise forms.ValidationError('Las password no es igual, vuelva a escribir la password') 
        value_pass

class SolicitarCitaForm(forms.Form):

    CIRUGIA_CHOICES = (
    ('P','Plastica'),
    ('C','Cardiovascular'),
        )
    CIRUGIA_MEDICO = (
    ('Pedro','Pedro'),
    ('jose','jose'),
    )

    cirugia = forms.ChoiceField(choices =CIRUGIA_CHOICES )
    medico = forms.ChoiceField(choices=CIRUGIA_MEDICO)
    fecha = forms.DateField()
