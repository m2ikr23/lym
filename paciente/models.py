from django.db import models
from users.models import User
# Create your models here.

class Paciente(User):

    PAIS_CHOICES=(
        ('ES','Espana'),
        ('EC','Ecuador'),
        ('USA','Estados Unidos'),        
    )

    pais = models.CharField(max_length=30,choices=PAIS_CHOICES)