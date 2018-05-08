from django.db import models
from users.models import User
# Create your models here.

class Paciente(User):

    PAIS_CHOICES=(
        ('ES','Espana'),
        ('EC','Ecuador'),
        ('USA','Estados Unidos'),        
    )
    codigo_Postal = models.CharField(max_length=16)
    pais = models.CharField(max_length=30,choices=PAIS_CHOICES)
    
    def setIs_Pacient(self):
        self.is_pacient = True


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
    paciente = models.OneToOneField(Paciente,on_delete=models.CASCADE)
    peso = models.FloatField()
    grupo_san = models.CharField(max_length=4, choices=GRUP_CHOICES,verbose_name='grupo sanguinio')
    tipo_aler = models.CharField(max_length=30,choices=ALERG_CHOICES)    
    cirugias_ant = models.TextField(max_length=150)
    patologia = models.CharField(max_length=50)
    observaciones = models.TextField(max_length=150)
   
    def __str__(self):
        return self.paciente
