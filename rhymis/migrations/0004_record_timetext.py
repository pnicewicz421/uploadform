# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0003_auto_20151127_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='timeText',
            field=models.DateTimeField(verbose_name='time case opened', default=datetime.datetime.now),
        ),
    ]
