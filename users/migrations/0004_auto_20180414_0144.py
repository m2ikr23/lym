# Generated by Django 2.0.3 on 2018-04-14 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180414_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='pais',
            field=models.CharField(choices=[('Es', 'ESPAÑA'), ('Ro', 'ROMA'), ('USA', 'ESTADOS UNIDOS')], max_length=2),
        ),
    ]