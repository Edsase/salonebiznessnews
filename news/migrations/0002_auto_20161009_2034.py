# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='feed',
            name='slug',
            field=models.SlugField(default='slug', unique=True),
            preserve_default=False,
        ),
    ]
