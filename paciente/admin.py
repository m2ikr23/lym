from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import CharField, Form, PasswordInput
from .models import Paciente,Paquete,Servicio,Solicitud_Paquete
# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    password = CharField(widget=PasswordInput())
    fieldsets = (
        ('User',{'fields':('email','password')}),
        ('Inf. personal',{'fields':('dni','first_name','last_name','birthdate','address','pais','codigo_Postal','phone','avatar')}),
        
    )
   
    
    add_fieldsets = (
        ('User',{'fields':('email','password')}),
        ('Inf. personal',{'fields':('dni','first_name','last_name','birthdate','address','pais','codigo_Postal','phone','avatar')}),
        
    )
    list_display = ['id','first_name','email']
    
    ordering = ['id']


admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Paquete)
admin.site.register(Servicio)
admin.site.register(Solicitud_Paquete)