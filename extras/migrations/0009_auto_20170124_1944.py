# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-24 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0008_images_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='grundriss',
            name='name',
            field=models.CharField(default='grundriss', max_length=250),
        ),
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default='video', max_length=250),
        ),
        migrations.AlterField(
            model_name='images',
            name='name',
            field=models.CharField(default='images', max_length=250),
        ),
    ]