from django.contrib import admin
from .models import Cirujano,Cirugia,Especialidad,Cirugia_Planificada,Cita,Historia
# Register your models here.
admin.site.register(Cirujano)
admin.site.register(Cirugia)
admin.site.register(Especialidad)
admin.site.register(Cirugia_Planificada)
admin.site.register(Cita)
admin.site.register(Historia)
