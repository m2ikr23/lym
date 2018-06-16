from django.db import models
from users.models import User
from clinica.models import Quirofano
from paciente.models import Paciente
from datetime import date

class Especialidad(models.Model):
    
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Cirujano(User):

    especialidad = models.ManyToManyField(Especialidad)
    def setIs_Medical(self):
        self.is_medical = True

    def __str__(self):
        if self.sex=='F':
            return '%s %s %s' %('Dra. ' , self.first_name, self.last_name)
        else:
            return '%s %s %s' %('Dra. ' , self.first_name, self.last_name)
 


class Cirugia(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=150)

    def __str__(self):
        return self.nombre


class Cirugia_Planificada(models.Model):
    cirugia = models.ForeignKey(Cirugia,on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today,unique=True)
    quirofano = models.ForeignKey(Quirofano,on_delete=models.CASCADE)
    cirujano = models.ForeignKey(Cirujano,on_delete=models.CASCADE)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=150)


class Agenda(models.Model):
  pass


