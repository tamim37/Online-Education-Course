# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-06 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_comments_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='userName2',
            field=models.CharField(max_length=90, null=True),
        ),
    ]
