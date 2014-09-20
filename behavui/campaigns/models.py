from django.db import models

from projects.models import Project
from features.models import Scenario

# Create your models here.
class Campaign(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    project     = models.ForeignKey(Project)
    scenarios    = models.ManyToManyField(Scenario)

    def __str__(self):
        return self.name
