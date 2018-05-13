from django.db import models
from users.models import User
 
from paciente.models import Paciente
# Create your models here.



class Especialidad(models.Model):
    
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Cirujano(User):

    especialidad = models.ManyToManyField(Especialidad,through='Cirujano_Especialidad')
    def setIs_Medical(self):
        self.is_medical = True

    def __str__(self):
        return self.first_name
 

class Cirujano_Especialidad(models.Model):

    cirujano = models.ForeignKey(Cirujano,on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad,on_delete=models.CASCADE)

class Cirugia(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=150)

    def __str__(self):
        return self.nombre


class Cirugia_Planificada(models.Model):
    cirugia = models.OneToOneField(Cirugia,on_delete=models.CASCADE)
    cirujano = models.ForeignKey(Cirujano,on_delete=models.CASCADE)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=150)


class Agenda(models.Model):
  pass


