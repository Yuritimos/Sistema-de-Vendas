# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160528_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='configuracao',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.Configuracao'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venda',
            name='configuracao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Configuracao'),
            preserve_default=False,
        ),
    ]
