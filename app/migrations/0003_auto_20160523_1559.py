# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160523_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='descricao',
            field=models.CharField(max_length=30, verbose_name='Descrição'),
        ),
    ]