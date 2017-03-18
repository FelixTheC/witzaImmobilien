# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 07:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makler', '0008_auto_20170115_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realestate',
            old_name='name',
            new_name='name_objekt',
        ),
        migrations.AddField(
            model_name='realestate',
            name='energieAusweis',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='makler.Energieausweis'),
            preserve_default=False,
        ),
    ]