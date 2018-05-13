from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from uuid import uuid4
from datetime import date
import os
class UserManager(BaseUserManager):

    def _create_user(self,email,password,is_staff,is_superuser,**extra_fields):

        if not email:
            return ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True, is_staff=is_staff,is_superuser=is_superuser,**extra_fields)

        user.set_password(password)
        user.save(using = self.db)
        return user


    def create_user(self,email,password=None,**extra_fields):
        return  self._create_user(email,password,False,False,**extra_fields)
   
    def create_superuser(self,email,password,**extra_fields):
        return self._create_user(email,password,True,True,**extra_fields)


class User (AbstractBaseUser,PermissionsMixin):
    
    GENERO_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino'),
    )

    email = models.CharField(max_length=50, unique=True)
    first_name=models.CharField(max_length=100,verbose_name='nombre')
    dni = models.CharField(max_length=16)
    last_name = models.CharField(max_length=100,verbose_name='apellido')
    phone = models.CharField(max_length=16,verbose_name='telefono')
    address = models.CharField(max_length=100, default=" ",verbose_name='direccion')
    birthdate = models.DateField(default= date.today,verbose_name='fecha de nacimiento' )
    avatar = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/user.png')
    is_pacient = models.BooleanField(default=False)
    is_medical = models.BooleanField(default=False)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        return self.first_name + " " + self.last_name

  
    def __str__(self):
        return self.first_name