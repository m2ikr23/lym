from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

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

    email = models.CharField(max_length=50, unique=True)
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=100, default="mi direccion")
    birthdate = models.DateField(auto_now=True)
    avatar = models.URLField()

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        return self.first_name

