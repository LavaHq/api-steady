# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-16 00:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [('steady', '0001_initial'), ]

    operations = [
        migrations.RemoveField(model_name='scoresheet',
                               name='user', ),
    ]
