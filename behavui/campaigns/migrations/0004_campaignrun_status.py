# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_xworkflows.models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_campaignrun'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignrun',
            name='status',
            field=django_xworkflows.models.StateField(max_length=16, workflow=django_xworkflows.models._SerializedWorkflow(states=['new', 'run', 'ok', 'nok'], initial_state='new', name='CampaignWorkflow')),
            preserve_default=True,
        ),
    ]
