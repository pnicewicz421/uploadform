# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0009_auto_20151127_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='datetimeText',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='date and time case opened'),
        ),
    ]
