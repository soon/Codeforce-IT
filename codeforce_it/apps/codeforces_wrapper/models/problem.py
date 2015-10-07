from django.db import models
from django.utils.translation import ugettext_lazy as _

from codeforce_it.apps.codeforces_wrapper.models import Contest


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class Problem(models.Model):
    cf_contest_id = models.IntegerField(verbose_name=_('Codeforces contest number'))
    cf_index = models.CharField(verbose_name=_('Codeforces problem index'), max_length=16)
    max_score = models.FloatField(verbose_name=_('Maximum amount of points'))
    contest = models.ForeignKey(Contest, null=True)

    class Meta:
        app_label = 'codeforces_wrapper'
        unique_together = ('cf_contest_id', 'cf_index', 'contest')
        ordering = ['max_score', 'id']

    @property
    def codeforces_url(self):
        return 'http://codeforces.com/problemset/problem/{}/{}'.format(self.cf_contest_id, self.cf_index)
