# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('steady', '0003_scoresheet_label'), ]

    operations = [
        migrations.RemoveField(model_name='scoresheet',
                               name='entries', ),
        migrations.AddField(model_name='scoresheet',
                            name='entries',
                            field=models.ManyToManyField(to='steady.Entry'), ),
    ]
