# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-16 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20160515_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
