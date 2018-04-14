from django.db import models
# Create your models here.

class Persona(models.Model):

    STATUS_CHOICES = (
    ('a', 'Active'),
    ('d', 'desactive'),
)
   
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fech_na = models.DateField()
    direccion = models.TextField(max_length=100)
    email = models.CharField(max_length=100,primary_key = True, unique=True)
    number = models.CharField(max_length=16)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        abstract = True


class Paciente(Persona):
    PAIS_CHOICES = (
        ('Es','ESPAÑA'),
        ('Ro','ROMA'),
        ('USA','ESTADOS UNIDOS'),

    )

    desc = models.TextField(max_length=150)
    pais = models.CharField(max_length=4, choices=PAIS_CHOICES )


    def __str__(self):
        return self.desc

class Cirujano(Persona):
    
    especialidad = models.TextField(max_length=100)

    def __str__(self):
        return self.especialidad
