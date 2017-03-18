# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-26 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0013_auto_20170126_0804'),
        ('makler', '0036_auto_20170125_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='immobilie',
            name='expose',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='extras.Expose'),
            preserve_default=False,
        ),
    ]