# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-10 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]