# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0006_auto_20170123_2124'),
        ('makler', '0025_auto_20170123_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='immobilie',
            name='grdriss',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='extras.Grundriss'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='immobilie',
            name='objekbesrbng',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='extras.Beschreibung'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='immobilie',
            name='video',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='extras.Video'),
            preserve_default=False,
        ),
    ]
