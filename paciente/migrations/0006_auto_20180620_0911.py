# Generated by Django 2.0.6 on 2018-06-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0005_servicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquete',
            name='servicios',
        ),
        migrations.AddField(
            model_name='paquete',
            name='servicios',
            field=models.ManyToManyField(to='paciente.Servicio'),
        ),
    ]