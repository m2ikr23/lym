from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import CharField, Form, PasswordInput
from .models import Paciente
# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    password = CharField(widget=PasswordInput())
    fieldsets = (
        ('User',{'fields':('email','password')}),
        ('Inf. personal',{'fields':('first_name','last_name','address','pais','phone','avatar')}),
        
    )
   
    
    add_fieldsets = (
        ('User',{'fields':('email','password')}),
        ('Inf. personal',{'fields':('first_name','last_name','address','pais','phone','avatar')}),
        
    )
    list_display = ['first_name','email']
    ordering = ['email']


admin.site.register(Paciente,PacienteAdmin)