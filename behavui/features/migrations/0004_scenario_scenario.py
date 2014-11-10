# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20140919_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='scenario',
            field=models.TextField(default='TODO'),
            preserve_default=False,
        ),
    ]
