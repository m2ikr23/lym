# Generated by Django 2.0.6 on 2018-06-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_auto_20180617_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete',
            name='servicios',
            field=models.CharField(choices=[('Traductora', 'Traductora'), ('Hospedaje', 'Hospedaje'), ('Transporte privado', 'Transporte privado'), ('Servicio Gastronomomico', 'Servicio Gastronómico'), ('Paseo por la Ciudad', 'Paseos por la ciudad')], max_length=50),
        ),
    ]
