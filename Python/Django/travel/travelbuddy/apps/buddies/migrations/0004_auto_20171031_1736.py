# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 06:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buddies', '0003_trip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='user_solo',
            new_name='traveler',
        ),
    ]
