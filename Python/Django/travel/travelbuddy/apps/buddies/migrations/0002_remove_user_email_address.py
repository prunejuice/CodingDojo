# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 06:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buddies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_address',
        ),
    ]
