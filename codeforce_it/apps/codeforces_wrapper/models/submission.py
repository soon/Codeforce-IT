from django.db import models
from django.utils.translation import ugettext_lazy as _

from codeforce_it.apps.codeforces_wrapper.models import Problem, Contestant


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class Submission(models.Model):
    VERDICT_FAILED = 'FAI'
    VERDICT_OK = 'OK'
    VERDICT_PARTIAL = 'PRT'
    VERDICT_COMPILATION_ERROR = 'CE'
    VERDICT_RUNTIME_ERROR = 'RE'
    VERDICT_WRONG_ANSWER = 'WA'
    VERDICT_PRESENTATION_ERROR = 'PE'
    VERDICT_TIME_LIMIT_EXCEEDED = 'TL'
    VERDICT_MEMORY_LIMIT_EXCEEDED = 'ML'
    VERDICT_IDLENESS_LIMIT_EXCEEDED = 'IL'
    VERDICT_SECURITY_VIOLATED = 'SV'
    VERDICT_CRASHED = 'CR'
    VERDICT_INPUT_PREPARATION_CRASHED = 'IPC'
    VERDICT_CHALLENGED = 'CLG'
    VERDICT_SKIPPED = 'SKP'
    VERDICT_TESTING = 'TST'
    VERDICT_REJECTED = 'REJ'

    VERDICT_CHOICES = (
        (VERDICT_FAILED, _('Failed')),
        (VERDICT_OK, _('OK')),
        (VERDICT_PARTIAL, _('Partial')),
        (VERDICT_COMPILATION_ERROR, _('Compilation error')),
        (VERDICT_RUNTIME_ERROR, _('Runtime error')),
        (VERDICT_WRONG_ANSWER, _('Wrong answer')),
        (VERDICT_PRESENTATION_ERROR, _('Representation error')),
        (VERDICT_TIME_LIMIT_EXCEEDED, _('Time limit exceeded')),
        (VERDICT_MEMORY_LIMIT_EXCEEDED, _('Memory limit exceeded')),
        (VERDICT_IDLENESS_LIMIT_EXCEEDED, _('Idleness limit exceeded')),
        (VERDICT_SECURITY_VIOLATED, _('Security violated')),
        (VERDICT_CRASHED, _('Crashed')),
        (VERDICT_INPUT_PREPARATION_CRASHED, _('Input preparation crashed')),
        (VERDICT_CHALLENGED, _('Challenged')),
        (VERDICT_SKIPPED, _('Skipped')),
        (VERDICT_TESTING, _('Testing')),
        (VERDICT_REJECTED, _('Rejected')),
    )

    cf_id = models.IntegerField(verbose_name=_('Codeforces Id'))
    problem = models.ForeignKey(Problem)
    author = models.ForeignKey(Contestant)
    creation_time = models.DateTimeField(verbose_name=_('Creation time'))
    verdict = models.CharField(verbose_name=_('Verdict'), choices=VERDICT_CHOICES, max_length=3)
