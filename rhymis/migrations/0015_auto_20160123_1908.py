# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0014_auto_20160123_0303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('locationName', models.TextField(default='', max_length='45')),
            ],
        ),
        migrations.RemoveField(
            model_name='record',
            name='recordNumberText',
        ),
        migrations.AlterField(
            model_name='record',
            name='locationText',
            field=models.ForeignKey(default=None, to='rhymis.Location'),
        ),
        migrations.DeleteModel(
            name='RecordNumber',
        ),
    ]
