from django import forms
from .models import User
class LoginForm(forms.Form):

    email = forms.EmailField(max_length=50, widget = forms.EmailInput)
    password = forms.CharField(max_length=20,min_length=8,widget = forms.PasswordInput())


class CreateForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(max_length=20,min_length=8,widget=forms.PasswordInput())
    birthdate = forms.CharField(widget=forms.DateInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','dni','birthdate','address',
                    'email','password']
