# Generated by Django 2.2.dev20180914183443 on 2018-10-16 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudio',
            name='relevancia',
        ),
        migrations.AddField(
            model_name='estudio',
            name='nombre',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='estudio',
            name='tipo',
            field=models.CharField(choices=[('FS', 'Fisico'), ('BIO', 'Biologico'), ('SC', 'Socio-Cultural')], default='', max_length=25),
        ),
        migrations.AddField(
            model_name='estudio',
            name='tipo_relevancia',
            field=models.CharField(choices=[('DI', 'Directo'), ('IN', 'Indirecto')], default='', max_length=25),
        ),
        migrations.AddField(
            model_name='estudio',
            name='valoracion_relevancia',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='duracion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='extension',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='intensidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='reversibilidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='via',
            field=models.FloatField(),
        ),
        migrations.DeleteModel(
            name='Duracion',
        ),
        migrations.DeleteModel(
            name='Extension',
        ),
        migrations.DeleteModel(
            name='Intensidad',
        ),
        migrations.DeleteModel(
            name='Relevancia',
        ),
        migrations.DeleteModel(
            name='Reversibilidad',
        ),
    ]
