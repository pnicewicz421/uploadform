# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0005_auto_20151127_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='locationText',
            field=models.CharField(choices=[('WP', 'Woodberry Park'), ('GB', 'Gates of Ballston'), ('FH', 'Fort Henry'), ('OT', 'Other')], max_length='30', default='OT'),
        ),
    ]
