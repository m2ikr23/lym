from django.forms import ModelForm
from django import forms
from users.forms import CreateForm as Create
from .models import Paciente,Paquete

class CreateForm(Create):

   
    class Meta:
        model = Paciente
        fields = ['first_name','last_name','dni','pais','phone','codigo_Postal','address','sex','birthdate',
                    'email','repeat_email','password','repeat_password']

    
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['pais'].widget.attrs.update( {'id':'select_pais',
                                                    'class':'select' } )
    


class CreatePaqueteForm(forms.ModelForm):

    class Meta:
        model = Paquete
        fields = ['id','nombre','servicios','precio']


class UpdatePaqueteForm(forms.ModelForm):

    class Meta: 
        model = Paquete
        fields = ['nombre','servicios','precio']


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
