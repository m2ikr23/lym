from django.db import models
# Create your models here.

class Persona(models.Model):

    STATUS_CHOICES = (
    ('A', 'Activo'),
    ('I', 'Inactivo'),
)
   
    GENERO_CHOICES = (
    ('F', 'Femenino'),
    ('M', 'Masculino'),
)
   
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    genero = models.CharField(max_length=1, choices= GENERO_CHOICES)
    fech_na = models.DateField()
    direccion = models.CharField(max_length=150)
    email = models.CharField(max_length=100,primary_key = True, unique=True)
    telefono = models.CharField(max_length=16)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        abstract = True


class Paciente(Persona):
    PAIS_CHOICES = (
        ('ES','ESPAÑA'),
        ('RO','ROMA'),
        ('USA','ESTADOS UNIDOS'),

    )

    pais = models.CharField(max_length=4, choices=PAIS_CHOICES )


    def __str__(self):
        return self.pais

class Cirujano(Persona):
    ESP_CHOICES = (
        ('ES','ESPAÑA'),
        ('RO','ROMA'),
        ('USA','ESTADOS UNIDOS'),

    )
    especialidad = models.TextField(max_length=100)

    def __str__(self):
        return self.especialidad
