# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0020_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='locations',
            field=models.ManyToManyField(to='rhymis.Location'),
        ),
    ]
