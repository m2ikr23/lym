from django.forms import ModelForm
from django import forms
from .models import Cirujano,Cirugia_Planificada,Cirugia,Especialidad,Historia,Cita
from users.forms import CreateForm as Create

class CreateForm(Create):

    class Meta:
        model = Cirujano
        fields = ['first_name','last_name','dni','sex','birthdate','especialidad','address','phone',
                    'email','repeat_email','password','repeat_password']

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['birthdate'].widget.attrs.update( {'id':'fecha_selec', 'class':'datepicker' } )

class PlanificarForm(forms.ModelForm):

    class Meta:
        model = Cirugia_Planificada
        fields = ['cirugia','fecha','quirofano','descripcion']

    def __init__(self, *args, **kwargs):
        super(PlanificarForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs.update( {'id':'fecha_select', 'class':'datepicker1' } )

class UpdateplanificacionForm(forms.ModelForm):

    class Meta:
        model = Cirugia_Planificada
        fields = ['cirugia','fecha','quirofano','descripcion']

class CreateCirugiaForm(forms.ModelForm):

    class Meta:
        model = Cirugia
        fields = ['id','nombre','tipo','descripcion']


class CreateEspecialidadForm(forms.ModelForm):

    class Meta:
        model = Especialidad
        fields = ['id','nombre','descripcion']

class UpdateCirugiaForm(forms.ModelForm):

    class Meta:

        model = Cirugia
        fields = ['nombre','tipo','descripcion']


class UpdateEspecialidadForm(forms.ModelForm):

    class Meta:

        model = Especialidad
        fields = ['nombre','descripcion']


class CrearHistoriaForm(forms.ModelForm):
  
    class Meta:
        model = Historia
        fields = ['peso','grupo_san','tipo_aler','cirugias_ant','patologia','observaciones']

 
class UpdateHistoriaForm(forms.ModelForm):

    class Meta:

        model = Historia
        fields = ['peso','grupo_san','tipo_aler','cirugias_ant','patologia','observaciones']



class ConfirmarForm(forms.ModelForm):

    class Meta:

        model = Cita
        fields = ['confirmada']
