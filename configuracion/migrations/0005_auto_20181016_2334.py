# Generated by Django 2.2.dev20180914183443 on 2018-10-16 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0004_auto_20181016_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudio',
            name='nombre',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]