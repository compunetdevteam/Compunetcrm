# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-21 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compunetcrm', '0018_auto_20180221_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image_description',
            field=models.CharField(max_length=255),
        ),
    ]
