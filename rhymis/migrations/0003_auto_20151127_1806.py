# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0002_auto_20151127_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='locationText',
        ),
        migrations.RemoveField(
            model_name='record',
            name='notesText',
        ),
        migrations.RemoveField(
            model_name='record',
            name='timeText',
        ),
        migrations.RemoveField(
            model_name='record',
            name='youthNameText',
        ),
    ]
