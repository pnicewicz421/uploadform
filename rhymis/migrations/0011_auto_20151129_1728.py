# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0010_auto_20151127_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordNumber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='record_number',
            field=models.ForeignKey(to='rhymis.RecordNumber', default=None),
        ),
    ]
