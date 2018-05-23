from django.forms import ModelForm
from django import forms
from users.forms import CreateForm as Create
from .models import Paciente

class CreateForm(Create):

   
    class Meta:
        model = Paciente
        fields = ['first_name','last_name','dni','pais','codigo_Postal','address','phone','sex','birthdate',
                    'email','repeat_email','password','repeat_password']



class SolicitarCitaForm(forms.Form):

    CIRUGIA_CHOICES = (
    ('P','Plastica'),
    ('C','Cardiovascular'),
        )
    CIRUGIA_MEDICO = (
    ('Pedro','Pedro'),
    ('jose','jose'),
    )

    def __init__(self, *args, **kwargs):
        super(SolicitarCitaForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs.update( {'id':'fecha_selec', 'class':'datepicker' } )

    cirugia = forms.ChoiceField(choices =CIRUGIA_CHOICES )
    medico = forms.ChoiceField(choices=CIRUGIA_MEDICO)
    fecha = forms.DateField()
