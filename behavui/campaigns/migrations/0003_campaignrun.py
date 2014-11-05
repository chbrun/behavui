# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django_xworkflows import models as xwf_models
import django.db.models.base


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20140919_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignRun',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('runAt', models.DateTimeField()),
                ('campaign', models.ForeignKey(to='campaigns.Campaign')),
            ],
            options={
            },
            bases=(xwf_models.WorkflowEnabled, models.Model),
        ),
    ]
