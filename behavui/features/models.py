from django.db import models

from projects.models import Project

# Create your models here.
class Feature(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    project     = models.ForeignKey(Project)

    def __str__(self):
        return self.name

class Scenario(models.Model):
    title        = models.CharField(max_length=100) 
    feature      = models.ForeignKey(Feature)
    precondition = models.TextField()
    auto         = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Step(models.Model):
    scenario = models.ForeignKey(Scenario)
    order    = models.PositiveIntegerField()
    action   = models.TextField()
    result   = models.TextField()

    def __str__(self):
        return "step %s de %s" % (str(self.order), self.scenario)

