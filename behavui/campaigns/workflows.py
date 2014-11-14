from django_xworkflows import models as xwf_models


class CampaignWorkflow(xwf_models.Workflow):
    log_model = ''

    states = (
        ('new', (u"New")),
        ('run', (u"Run")),
        ('ok', (u"OK")),
        ('nok', (u"NOK")),
    )

    transitions = (
        ('start', 'new', 'run'),
        ('doneOK', 'run', 'ok'),
        ('doneNOK', 'run', 'nok'),
    )

    initial_state = 'new'
