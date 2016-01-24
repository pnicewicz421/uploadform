# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0013_auto_20160122_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='datetimeText',
            field=models.TextField(max_length='30'),
        ),
    ]
