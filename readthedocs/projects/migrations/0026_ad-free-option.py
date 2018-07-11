# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-29 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_show-version-warning-existing-projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ad_free',
            field=models.BooleanField(default=False, help_text='If checked, do not show advertising for this project', verbose_name='Ad-free'),
        ),
    ]
