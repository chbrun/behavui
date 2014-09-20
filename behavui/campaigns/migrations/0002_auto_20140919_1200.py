# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20140919_1154'),
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='features',
        ),
        migrations.AddField(
            model_name='campaign',
            name='scenarios',
            field=models.ManyToManyField(to='features.Scenario'),
            preserve_default=True,
        ),
    ]
