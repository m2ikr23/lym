from django import forms
from .models import User
class LoginForm(forms.Form):

    email = forms.EmailField( widget = forms.EmailInput)
    password = forms.CharField(max_length=20,min_length=8,widget = forms.PasswordInput())


class CreateForm(forms.ModelForm):
    email = forms.EmailField( widget = forms.EmailInput)
    password = forms.CharField(max_length=20,min_length=8,widget=forms.PasswordInput())
    repeat_password = forms.CharField(max_length=20,min_length=8,widget=forms.PasswordInput())
    birthdate = forms.CharField(widget=forms.DateInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','dni','birthdate','address',
                    'email','password']

    def clean_repeat_password(self):
        value_pass = self.cleaned_data['password']
        value_pass2 = self.cleaned_data['repeat_password']
        if value_pass2 != value_pass:
            raise forms.ValidationError('Las password no es igual, vuelva a escribir la password') 
        value_pass


class ImageUploadForm(forms.ModelForm):
    """Image upload form."""
    avatar = forms.ImageField()
    class Meta:
        model = User
        fields= ['avatar']


class UpdateUserForm(forms.ModelForm):

    password = forms.CharField(max_length=20,min_length=8,widget=forms.PasswordInput())
    repeat_password = forms.CharField(max_length=20,min_length=8,widget=forms.PasswordInput())
    birthdate = forms.CharField(widget=forms.DateInput)

    class Meta:

        model = User
        fields = ['first_name','last_name','address','phone','birthdate','password']
   
    def clean_repeat_password(self):
        value_pass = self.cleaned_data['password']
        value_pass2 = self.cleaned_data['repeat_password']
        if value_pass2 != value_pass:
            raise forms.ValidationError('Los campos de password no coinciden, verifiquelos') 
        value_pass