# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-20 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compunetcrm', '0011_auto_20180220_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetextcordinate',
            name='alt_text',
            field=models.CharField(max_length=400, verbose_name='Image Alt Text'),
        ),
        migrations.AlterField(
            model_name='imagetextcordinate',
            name='link',
            field=models.CharField(max_length=700, verbose_name='Image URL'),
        ),
    ]
