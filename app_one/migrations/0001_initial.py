# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('age', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]