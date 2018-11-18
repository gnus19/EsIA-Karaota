# Generated by Django 2.1.2 on 2018-11-08 18:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181108_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='doc_identidad',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[VEF]-\\d+$', 'Formato de documento de identidad inválido. Los números deben estar precedidos por V- o E-.')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Apellido'),
        ),
    ]
