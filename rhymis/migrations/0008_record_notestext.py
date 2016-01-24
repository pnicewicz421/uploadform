# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0007_record_youthnametext'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='notesText',
            field=models.TextField(default=''),
        ),
    ]
