# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='juanito', max_length=50)),
                ('apellido', models.CharField(default='', max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('semestre', models.IntegerField()),
                ('carrera', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=2)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]
