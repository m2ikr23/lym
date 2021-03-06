from django.db import models
from datetime import date

class Clinica(models.Model):

    id = models.CharField(max_length=8,primary_key="True")
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=16)
    email = models.EmailField(max_length = 50, unique=True)
    is_active = models.BooleanField(default = True)

    def __str__(self):
    
        return self.nombre

    def idNombre(self):

        return '%s - %s' %(self.id ,self.nombre)


class Quirofano(models.Model):

    id = models.CharField(max_length=8,primary_key="True")
    clinica = models.ForeignKey(Clinica,on_delete=models.CASCADE,limit_choices_to= {'is_active':True} )
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=150)
    is_active = models.BooleanField(default = True)

    def __str__(self):
    
        return self.nombre 
        
    def idNombre(self):

        return '%s - %s' %(self.id ,self.nombre)