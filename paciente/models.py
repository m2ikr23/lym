from django.db import models
from users.models import User,Country

class Paciente(User):

    codigo_Postal = models.CharField(max_length=16)
    pais = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def setIs_Pacient(self):
        self.is_pacient = True



class Paquete(models.Model):
 
    id = models.CharField(max_length=8,primary_key=True)
    nombre = models.CharField(max_length=50)
    servicios = models.ManyToManyField('Servicio')
    precio = models.IntegerField()

    def __str__(self):
        return '%s: %s- $ %s ' %(self.nombre,self.strServicio() ,self.precio)

    def strServicio(self):
        servicio=""
        for serv in self.servicios.all():
            servicio +=' ' + serv.nombre+'-'
        return servicio

class Servicio(models.Model):

    nombre = models.CharField(max_length=120, verbose_name="Nombre")
    descripcion = models.TextField(max_length=150, verbose_name="Descripción")
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class Solicitud_Paquete(models.Model):
    
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete,on_delete=models.CASCADE)
    fecha_solicitada= models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return '%s - %s' %(self.paciente, self.paquete)
