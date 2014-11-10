# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django_xworkflows.models import StateField, _SerializedWorkflow


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_campaignrun'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignrun',
            name='status',
            field=StateField(max_length=16, workflow=_SerializedWorkflow(states=['new', 'run', 'ok', 'nok'], initial_state='new', name='CampaignWorkflow')),
            preserve_default=True,
        ),
    ]
