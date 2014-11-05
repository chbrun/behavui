from django.db import models

from projects.models import Project
from features.models import Scenario
from django_xworkflows import models as xwf_models
from .workflows import CampaignWorkflow

# Create your models here.
class Campaign(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    project     = models.ForeignKey(Project)
    scenarios   = models.ManyToManyField(Scenario)

    def __str__(self):
        return self.name

class CampaignRun(xwf_models.WorkflowEnabled, models.Model):
    runAt    = models.DateTimeField()
    campaign = models.ForeignKey(Campaign)
    status   = xwf_models.StateField(CampaignWorkflow)
