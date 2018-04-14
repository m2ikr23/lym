from django.contrib import admin

from .models import Paciente, Cirujano

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombres','apellidos','email','direccion','pais','number','status')


class CirujanoAdmin(admin.ModelAdmin):
    
    list_display = ('nombres','apellidos','email','status','especialidad')


admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Cirujano, CirujanoAdmin)




