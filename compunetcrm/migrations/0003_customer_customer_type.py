# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-14 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compunetcrm', '0002_auto_20180214_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_type',
            field=models.CharField(blank=True, choices=[('SCHOOL OWNER', 'MALE'), ('BSC STUDENT', 'FEMALE'), ('SIWES STUDENT', 'FEMALE'), ('WEEKEND TRAINING', 'FEMALE'), ('GENERAL ENQUIRIES', 'FEMALE'), ('COMPUNET STAFF', 'FEMALE')], max_length=10, verbose_name='Sex'),
        ),
    ]
