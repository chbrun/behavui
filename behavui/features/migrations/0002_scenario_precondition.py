# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='precondition',
            field=models.TextField(default='TODO'),
            preserve_default=False,
        ),
    ]
