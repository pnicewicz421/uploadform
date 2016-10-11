# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymis', '0017_document'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Document',
            new_name='FileUpload',
        ),
    ]
