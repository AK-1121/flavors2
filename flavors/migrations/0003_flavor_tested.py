# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flavors', '0002_flavor_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavor',
            name='tested',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
