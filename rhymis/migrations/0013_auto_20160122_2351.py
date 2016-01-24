# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0012_auto_20151129_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='datetimeText',
            field=models.DateField(verbose_name='date and time case opened', default=None, blank=True),
        ),
    ]
