# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-22 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0003_remove_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
