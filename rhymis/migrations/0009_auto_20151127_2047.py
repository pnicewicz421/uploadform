# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0008_record_notestext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='datetimeText',
            field=models.DateTimeField(verbose_name='date and time case opened', default=None, null=True),
        ),
    ]
