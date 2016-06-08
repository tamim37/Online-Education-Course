# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-23 07:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_auto_20160516_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=30, verbose_name="person's first name")),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.CourseMetarial')),
            ],
        ),
    ]