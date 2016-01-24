# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0015_auto_20160123_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='staffText',
            field=models.TextField(default=''),
        ),
    ]
