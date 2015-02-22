# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flavors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavor',
            name='color',
            field=models.CharField(max_length=200, default='xxx'),
            preserve_default=True,
        ),
    ]
