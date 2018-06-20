# Generated by Django 2.0.6 on 2018-06-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('servicios', models.CharField(choices=[('Trad', 'Traductora'), ('Hosp', 'Hospedaje'), ('Trans', 'Transporte privado'), ('SG', 'Servicio Gastronómico'), ('PC', 'Paseos por la ciudad')], max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]