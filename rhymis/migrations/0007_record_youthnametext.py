# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0006_record_locationtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='youthNameText',
            field=models.TextField(default=''),
        ),
    ]
