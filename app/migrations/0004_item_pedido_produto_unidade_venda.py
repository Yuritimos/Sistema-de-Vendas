# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160523_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=30, verbose_name='produto')),
                ('quantidade', models.IntegerField(default=0, verbose_name='quantidade')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, default='produto/no_foto.jpg', null=True, upload_to='produto/')),
                ('descricao', models.CharField(max_length=30, verbose_name='descricao')),
                ('unidade', models.IntegerField(default=0, verbose_name='unidade')),
                ('estoque', models.IntegerField(default=0, verbose_name='estoque')),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, verbose_name='descricao')),
                ('fator', models.IntegerField(default=0, verbose_name='fator')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Item')),
            ],
        ),
    ]
