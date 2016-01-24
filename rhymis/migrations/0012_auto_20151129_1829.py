# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0011_auto_20151129_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='record_number',
            new_name='recordNumberText',
        ),
    ]
