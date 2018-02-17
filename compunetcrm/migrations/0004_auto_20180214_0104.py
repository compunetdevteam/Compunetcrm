# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-14 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compunetcrm', '0003_customer_customer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_type',
            field=models.CharField(blank=True, choices=[('SCHOOL OWNER', 'SCHOOL OWNER'), ('BSC STUDENT', 'BSC STUDENT'), ('SIWES STUDENT', 'SIWES STUDENT'), ('WEEKEND TRAINING', 'WEEKEND TRAINING'), ('GENERAL ENQUIRIES', 'GENERAL ENQUIRIES'), ('INTERN', 'INTERN'), ('COMPUNET STAFF', 'COMPUNET STAFF')], max_length=10, verbose_name='Customer Type'),
        ),
    ]