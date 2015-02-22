# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flavors2', '0002_flavorreview_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavorreview',
            name='title',
            field=models.ForeignKey(to='flavors.Flavor'),
            preserve_default=True,
        ),
    ]
