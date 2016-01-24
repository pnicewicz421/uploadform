# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='dateText',
            field=models.DateField(verbose_name='date case opened', default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='record',
            name='locationText',
            field=models.CharField(choices=[('WP', 'Woodberry Park'), ('GB', 'Gates of Ballston'), ('FH', 'Fort Henry'), ('OT', 'Other')], max_length='30', default='OT'),
        ),
        migrations.AddField(
            model_name='record',
            name='notesText',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='record',
            name='timeText',
            field=models.DateTimeField(verbose_name='time case opened', default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='record',
            name='youthNameText',
            field=models.TextField(default=''),
        ),
    ]
