# Generated by Django 2.2.dev20180914183443 on 2018-10-16 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_auto_20181016_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudio',
            name='valoracion_relevancia',
            field=models.CharField(choices=[('A', 'Alto'), ('M', 'Medio'), ('Bajo', 'Bajo')], default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='via',
            field=models.FloatField(default=0.0),
        ),
    ]
