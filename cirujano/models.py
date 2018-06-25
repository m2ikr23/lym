from django.db import models
from users.models import User
from clinica.models import Quirofano,Clinica
from paciente.models import Paciente
from datetime import date

class Especialidad(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
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
            return '%s %s %s' %('Dr. ' , self.first_name, self.last_name)
 


class Cirugia(models.Model):
    TIPO=(
        ('OM','Cirugía Oral y Maxilofacial'),
        ('OO','Oftalmología y Oculopatía'),
        ('OT','Otorrinolaringología'),
        ('T','Traumatología'),
        ('PE','Cirugía plastica y estética'),
        ('U','Urología'),
        ('CG','Cirugía General')
    )
    id = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=50,choices=TIPO)
    descripcion = models.TextField(max_length=150)

    def __str__(self):
        return self.nombre


class Cirugia_Planificada(models.Model):
    cirugia = models.ForeignKey(Cirugia,on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today,unique=True,verbose_name='Fecha para la cirugía')
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    quirofano = models.ForeignKey(Quirofano,on_delete=models.CASCADE)
    cirujano = models.ForeignKey(Cirujano,on_delete=models.CASCADE)
    paciente = models.OneToOneField('Cita', on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=150)

    def __str__(self):
        return '%s - %s' %(self.fecha,self.paciente.paciente)

class Agenda(models.Model):
  pass


class Cita(models.Model):

    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Cirujano,on_delete=models.CASCADE,verbose_name="Médico cirujano",)
    fecha_solicitud = models.DateField(auto_now_add=True)
    confirmada = models.BooleanField(default=False)
    descripcion = models.TextField(max_length=150,verbose_name="Descripción")

    def __str__(self):

        return self.descripcion


class Historia(models.Model):
    GRUP_CHOICES = (
        ('A+','A+'),('A-','A-'),
        ('B+','B+'),('B-','B-'),
        ('AB+','AB+'),('AB-','AB-'),
        ('O+','O+'),('O-','O-'),
    )

    ALERG_CHOICES=(
        ('DC','Dermatitis de contacto'),
        ('AA','Alergia a los alimentos'),
        ('AM','Alergia a los medicamentos'),
    )
    
    paciente = models.OneToOneField(Cita,on_delete=models.CASCADE)
    medico = models.ForeignKey(Cirujano,on_delete=models.CASCADE)
    peso = models.FloatField(verbose_name='Peso')
    grupo_san = models.CharField(max_length=4, choices=GRUP_CHOICES,verbose_name='Grupo sanguínio')
    tipo_aler = models.CharField(max_length=30,choices=ALERG_CHOICES,verbose_name='Tipo de Alergias')    
    cirugias_ant = models.TextField(max_length=150,verbose_name='Cirugias anteriores')
    patologia = models.CharField(max_length=50,verbose_name='Patologia')
    observaciones = models.TextField(max_length=150,verbose_name='Observaciones')
   
    def __str__(self):
         return self.observaciones