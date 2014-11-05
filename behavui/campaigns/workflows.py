from django_xworkflows import models as xwf_models
from django.utils.translation import ugettext as _

class CampaignWorkflow(xwf_models.Workflow):
    log_model = ''

    states = (
        ('new', _(u"New")),
        ('run', _(u"Run")),
        ('ok' , _(u"OK")),
        ('nok', _(u"NOK")),
        )

    transitions = (
        ('start'  , 'new', 'run'),
        ('doneOK' , 'run', 'ok'),
        ('doneNOK', 'run', 'nok'),
        )

    initial_state = 'new'
