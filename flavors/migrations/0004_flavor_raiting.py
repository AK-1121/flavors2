# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flavors', '0003_flavor_tested'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavor',
            name='raiting',
            field=models.CharField(default=('0', 'x'), max_length=10, choices=[('0', 'x'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
            preserve_default=True,
        ),
    ]
