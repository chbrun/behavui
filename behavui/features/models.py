from django.db import models

from projects.models import Project

# Create your models here.
class Feature(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    project     = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    def get_script(self):
        script = ()
        for scenario in self.scenario_set.all():
            script += (scenario.get_script(),)
        return str.join('\r\r', script)


class Scenario(models.Model):
    title        = models.CharField(max_length = 100)
    feature      = models.ForeignKey(Feature)
    precondition = models.TextField()
    auto         = models.BooleanField(default = False)
    scenario     = models.TextField()

    def __str__(self):
        return self.title

    def get_script(self):
        retour = ()
        retour += ("Scenario: %s" % self.title,)
        retour += ("%s" % self.precondition,)
        for step in self.step_set.all():
            for ligne in step.action.split('\n'):
                retour += ("    %s" % ligne,)
            for ligne in step.result.split('\n'):
                retour += ("    %s" % ligne,)
        script = [x.replace("\r",'').replace('\n','') for x in retour if str.strip(x)!='']
        return str.join('\r',script)


class Step(models.Model):
    scenario = models.ForeignKey(Scenario)
    order    = models.PositiveIntegerField()
    action   = models.TextField()
    result   = models.TextField()

    def __str__(self):
        return "step %s de %s" % (str(self.order), self.scenario)

