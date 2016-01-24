# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0004_record_timetext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='dateText',
        ),
        migrations.RemoveField(
            model_name='record',
            name='timeText',
        ),
        migrations.AddField(
            model_name='record',
            name='datetimeText',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date and time case opened'),
        ),
    ]
