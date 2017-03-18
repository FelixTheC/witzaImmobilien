# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makler', '0024_auto_20170123_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='immobilie',
            name='verkauft',
        ),
        migrations.AddField(
            model_name='immobilie',
            name='immobilienArt',
            field=models.CharField(choices=[('EFH', 'Einfamilienhaus'), ('WE', 'Wohnung eigennutzung'), ('WK', 'Wohnung kapitalanlage'), ('MFH', 'Mehrfamilienhaus'), ('GR', 'Grundstück'), ('GEW', 'Gewerbe'), ('VK', 'Verkauft')], default=0, max_length=3),
            preserve_default=False,
        ),
    ]