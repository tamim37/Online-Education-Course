# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-06 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_crstaken'),
    ]

    operations = [
        migrations.AddField(
            model_name='crstaken',
            name='crsname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]