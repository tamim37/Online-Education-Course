# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20160429_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='option1',
            field=models.CharField(default='anonymous', max_length=50, null=True),
        ),
    ]