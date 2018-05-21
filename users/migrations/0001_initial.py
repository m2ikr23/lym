# Generated by Django 2.0.5 on 2018-05-21 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='nombre')),
                ('dni', models.CharField(max_length=16)),
                ('last_name', models.CharField(max_length=100, verbose_name='apellido')),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=2, verbose_name='sexo')),
                ('phone', models.CharField(max_length=16, verbose_name='telefono')),
                ('address', models.CharField(default=' ', max_length=100, verbose_name='direccion')),
                ('birthdate', models.DateField(default=datetime.date.today, verbose_name='fecha de nacimiento')),
                ('avatar', models.ImageField(default='pic_folder/None/user.png', upload_to='pic_folder/')),
                ('is_pacient', models.BooleanField(default=False)),
                ('is_medical', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
