# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 12:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autentificacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CruceMatriz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'cruce_matriz',
            },
        ),
        migrations.CreateModel(
            name='EquipoTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('J', 'Jefe de proyecto'), ('A', 'Analista'), ('D', 'Diseñador'), ('P', 'Programador'), ('T', 'Tester')], default='P', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140, verbose_name='Nombre del Proyecto')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripción del Proyecto')),
                ('fecha_creacion', models.DateField(default=django.utils.timezone.now, help_text='Indica la fecha de creación del Proyecto', verbose_name='Fecha de Creación')),
                ('fecha_finalizacion', models.DateField(help_text='Indica la fecha de finalización del Proyecto', null=True, verbose_name='Fecha de Finalización')),
                ('terminado', models.BooleanField(default=False, verbose_name='Terminado')),
                ('equipo_trabajo', models.ManyToManyField(through='seguimiento.EquipoTrabajo', to='autentificacion.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('descripcion', models.TextField(blank=True, default='')),
                ('tipo', models.CharField(choices=[('U', 'Usuario'), ('S', 'Software')], default='U', max_length=1)),
                ('cruce_matriz', models.ManyToManyField(blank=True, through='seguimiento.CruceMatriz', to='seguimiento.Requisito')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('avance', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('cruce_matriz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.CruceMatriz')),
            ],
        ),
        migrations.AddField(
            model_name='equipotrabajo',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.Proyecto'),
        ),
        migrations.AddField(
            model_name='equipotrabajo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autentificacion.Usuario'),
        ),
        migrations.AddField(
            model_name='crucematriz',
            name='from_requisito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_requisito', to='seguimiento.Requisito'),
        ),
        migrations.AddField(
            model_name='crucematriz',
            name='to_requisito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_requisito', to='seguimiento.Requisito'),
        ),
        migrations.CreateModel(
            name='RequisitoSoftware',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('seguimiento.requisito',),
        ),
        migrations.CreateModel(
            name='RequisitoUsuario',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('seguimiento.requisito',),
        ),
    ]
