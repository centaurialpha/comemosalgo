# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('disponibilidad', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Capacidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=150)),
                ('precio', models.FloatField()),
                ('disponibilidad', models.BooleanField()),
                ('categoria', models.ManyToManyField(to='producto.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen_Bebida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='img_bebidas')),
                ('bebida', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='producto.Bebida')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen_Comida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='img_comidas')),
                ('comida', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='producto.Comida')),
            ],
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='bebida',
            name='capacidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Capacidad'),
        ),
        migrations.AddField(
            model_name='bebida',
            name='linea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Linea'),
        ),
    ]
