# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 07:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makler', '0010_auto_20170117_0724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realestate',
            old_name='name_objekt',
            new_name='name',
        ),
    ]
