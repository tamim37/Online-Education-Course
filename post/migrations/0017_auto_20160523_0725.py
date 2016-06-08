# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-23 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300, verbose_name="person's first name")),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='comments',
        ),
        migrations.AddField(
            model_name='blog',
            name='commentsList',
            field=models.ManyToManyField(blank=True, to='post.Comments'),
        ),
    ]