# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-21 02:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Qrious', '0009_questions_questions_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='questions_img',
        ),
    ]
