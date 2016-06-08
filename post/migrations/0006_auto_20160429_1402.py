# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20160429_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizNo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='option1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='quizsection',
            name='questionList',
            field=models.ManyToManyField(to='post.QuizQuestion'),
        ),
    ]
