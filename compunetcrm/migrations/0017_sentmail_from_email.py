# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-21 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compunetcrm', '0016_sentmail_image_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentmail',
            name='from_email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
