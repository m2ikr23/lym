# Generated by Django 2.0.6 on 2018-06-24 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cirujano', '0003_cita_confirmada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='confirmada',
            field=models.BooleanField(default=False),
        ),
    ]
