# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 18:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makler', '0017_auto_20170122_0110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realestate',
            old_name='pic1',
            new_name='bild',
        ),
    ]
