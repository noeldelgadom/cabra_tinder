# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_auto_20170503_0139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goat',
            old_name='age',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='goat',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='goat',
            old_name='description',
            new_name='sexy_quote',
        ),
        migrations.AddField(
            model_name='goat',
            name='diagnostico',
            field=models.CharField(default='None', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goat',
            name='raza',
            field=models.CharField(default='None', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goat',
            name='sexo',
            field=models.CharField(default='Macho', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goat',
            name='profile_pic',
            field=models.CharField(max_length=300),
        ),
    ]