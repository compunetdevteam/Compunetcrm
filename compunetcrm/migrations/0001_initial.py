# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-13 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Surname')),
                ('mothers_maiden_name', models.CharField(blank=True, max_length=40, verbose_name='Mothers Maiden Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('state', models.CharField(choices=[('ABIA', 'ABIA'), ('ADAMAWA', 'ADAMAWA'), ('AKWAIBOM', 'AKWAIBOM'), ('ANAMBRA', 'ANAMBRA'), ('BAUCHI', 'BAUCHI'), ('BAYELSA', 'BAYELSA'), ('BENUE', 'BENUE'), ('BORNO', 'BORNO'), ('CROSSRIVERS', 'CROSSRIVERS'), ('DELTA', 'DELTA'), ('EBONYI', 'EBONYI'), ('EDO', 'EDO'), ('EKITI', 'EKITI'), ('ENUGU', 'ENUGU'), ('GOMBE', 'GOMBE'), ('IMO', 'IMO'), ('JIGAWA', 'JIGAWA'), ('KADUNA', 'KADUNA'), ('KANO', 'KANO'), ('KATSINA', 'KATSINA'), ('KEBBI', 'KEBBI'), ('KOGI', 'KOGI'), ('KWARA', 'KWARA'), ('LAGOS', 'LAGOS'), ('NASARAWA', 'NASARAWA'), ('NIGER', 'NIGER'), ('OGUN', 'OGUN'), ('ONDO', 'ONDO'), ('OSUN', 'OSUN'), ('OYO', 'OYO'), ('PLATEAU', 'PLATEAU'), ('RIVERS', 'RIVERS'), ('SOKOTO', 'SOKOTO'), ('TARABA', 'TARABA'), ('YOBE', 'YOBE'), ('ZAMFARA', 'ZAMFARA')], max_length=100, verbose_name='State')),
                ('local_government', models.CharField(max_length=70, verbose_name='Local Government')),
                ('sex', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10, verbose_name='Sex')),
                ('district', models.CharField(blank=True, max_length=600, verbose_name='District')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('communication_means1', models.NullBooleanField(verbose_name='E-mail')),
                ('communication_means2', models.NullBooleanField(verbose_name='Phone')),
            ],
        ),
    ]