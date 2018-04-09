from django.db import models
# Create your models here.

class Persona(models.Model):

    length=100
    STATUS_CHOICES = (
    ('a', 'Active'),
    ('d', 'desactive'),
)
    firstname = models.CharField(max_length=length)
    lastname = models.CharField(max_length=length)
    birtday = models.DateField() 
    email = models.CharField(max_length=length,primary_key = True, unique=True)
    number = models.CharField(max_length=16)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        abstract = True


class Paciente(Persona):
    
    desc = models.TextField(max_length=150)

    def __str__(self):
        return self.desc

class Cirujano(Persona):
    
    especialidad = models.TextField(max_length=100)

    def __str__(self):
        return self.especialidad
