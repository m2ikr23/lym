from django import forms
from .models import User,Country
class LoginForm(forms.Form):

    email = forms.EmailField( widget = forms.EmailInput)
    password = forms.CharField(max_length=20,min_length=8,widget = forms.PasswordInput())


class CreateForm(forms.ModelForm):
    email = forms.EmailField()
    repeat_email = forms.EmailField(widget = forms.EmailInput,
                                        label="Verificar email")
    password = forms.CharField(max_length=20,min_length=8,
                                    widget=forms.PasswordInput())
    repeat_password = forms.CharField(max_length=20,min_length=8,
                                         widget=forms.PasswordInput(),
                                                label="Verificar password ")
    birthdate = forms.CharField(widget=forms.DateInput,label='Fecha de nacimiento')
    class Meta:
        model = User
        fields = ['first_name','last_name','dni','address','phone','sex','birthdate',
                    'email','repeat_email','password','repeat_password']


    def clean_repeat_email(self):
        value_email = self.cleaned_data['email']
        value_email2 = self.cleaned_data['repeat_email']
        if value_email2 != value_email:
            raise forms.ValidationError('El email no es igual, vuelva a escribir el email') 
        value_email


    def clean_repeat_password(self):
        value_pass = self.cleaned_data['password']
        value_pass2 = self.cleaned_data['repeat_password']
        if value_pass2 != value_pass:
            raise forms.ValidationError('Las password no es igual, vuelva a escribir la password') 
        value_pass
    

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['birthdate'].widget.attrs.update( {'id':'fecha_selec',
                                                    'class':'datepicker' } )                         

class ImageUploadForm(forms.ModelForm):
    """Image upload form."""
    avatar = forms.ImageField()
    class Meta:
        model = User
        fields= ['avatar']


class UpdateUserForm(forms.ModelForm):

    password = forms.CharField(max_length=20,min_length=8,widget=forms.PasswordInput(),required=False)
    repeat_password = forms.CharField(max_length=20,min_length=8,widget=forms.PasswordInput(),required=False, label="Verificar password")
    birthdate = forms.CharField(widget=forms.DateInput(format='%Y-%m-%d'),label="Fecha de nacimiento")

    class Meta:

        model = User
        fields = ['first_name','last_name','address','phone','birthdate','password']
   
    def clean_repeat_password(self):
        value_pass = self.cleaned_data['password']
        value_pass2 = self.cleaned_data['repeat_password']
        if value_pass2 != value_pass:
            raise forms.ValidationError('Los campos de password no coinciden, verifiquelos') 
        value_pass

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['birthdate'].widget.attrs.update( {'id':'fecha_selec', 'class':'datepicker' } )

class DesactivateUserForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['is_active']
   