# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flavors', '0004_flavor_raiting'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavor',
            name='short_title',
            field=models.SlugField(default=''),
            preserve_default=True,
        ),
    ]
