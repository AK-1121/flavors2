# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flavors', '0005_flavor_short_title'),
        ('flavors2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavorreview',
            name='title',
            field=models.ForeignKey(to='flavors.Flavor', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flavorreview',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flavorreview',
            name='review',
            field=models.CharField(max_length=255, default=''),
            preserve_default=True,
        ),
    ]
