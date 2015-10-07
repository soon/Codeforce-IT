from datetime import datetime

from codeforces import VerdictType
from django.db import models
from django.utils.timezone import make_aware, get_default_timezone
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

    cf_id = models.IntegerField(verbose_name=_('Codeforces Id'), unique=True)
    problem = models.ForeignKey(Problem)
    author = models.ForeignKey(Contestant)
    creation_time = models.DateTimeField(verbose_name=_('Creation time'))
    verdict = models.CharField(verbose_name=_('Verdict'), choices=VERDICT_CHOICES, max_length=3)

    class Meta:
        app_label = 'codeforces_wrapper'
        ordering = ['creation_time']

    @staticmethod
    def from_cf_submission(cf_submission, problem, author):
        assert cf_submission.problem.contest_id == problem.cf_contest_id
        assert cf_submission.problem.index == problem.cf_index
        assert len(cf_submission.author.members) == 1
        assert cf_submission.author.members[0].handle == author.cf_handle

        return Submission(cf_id=cf_submission.id, problem=problem, author=author,
                          creation_time=make_aware(datetime.fromtimestamp(cf_submission.creation_time),
                                                   get_default_timezone()),
                          verdict=Submission.parse_cf_verdict(cf_submission.verdict))

    @staticmethod
    def parse_cf_verdict(verdict_type):
        return {
            VerdictType.failed: Submission.VERDICT_FAILED,
            VerdictType.ok: Submission.VERDICT_OK,
            VerdictType.partial: Submission.VERDICT_PARTIAL,
            VerdictType.compilation_error: Submission.VERDICT_COMPILATION_ERROR,
            VerdictType.runtime_error: Submission.VERDICT_RUNTIME_ERROR,
            VerdictType.wrong_answer: Submission.VERDICT_WRONG_ANSWER,
            VerdictType.presentation_error: Submission.VERDICT_PRESENTATION_ERROR,
            VerdictType.time_limit_exceeded: Submission.VERDICT_TIME_LIMIT_EXCEEDED,
            VerdictType.memory_limit_exceeded: Submission.VERDICT_MEMORY_LIMIT_EXCEEDED,
            VerdictType.idleness_limit_exceeded: Submission.VERDICT_IDLENESS_LIMIT_EXCEEDED,
            VerdictType.security_violated: Submission.VERDICT_SECURITY_VIOLATED,
            VerdictType.crashed: Submission.VERDICT_CRASHED,
            VerdictType.input_preparation_crashed: Submission.VERDICT_INPUT_PREPARATION_CRASHED,
            VerdictType.challenged: Submission.VERDICT_CHALLENGED,
            VerdictType.skipped: Submission.VERDICT_SKIPPED,
            VerdictType.testing: Submission.VERDICT_TESTING,
            VerdictType.rejected: Submission.VERDICT_REJECTED
        }[verdict_type]
