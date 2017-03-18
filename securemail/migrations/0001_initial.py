# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaveContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=254)),
                ('gesendetAm', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
