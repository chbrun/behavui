# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_scenario_precondition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='order',
            field=models.PositiveIntegerField(),
        ),
    ]
