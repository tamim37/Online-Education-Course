# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-16 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_demo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to=b'')),
                ('weekNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Week')),
            ],
        ),
    ]
