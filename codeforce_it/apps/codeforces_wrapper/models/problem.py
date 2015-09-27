from django.db import models
from django.utils.translation import ugettext_lazy as _

__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class Problem(models.Model):
    cf_contest_id = models.IntegerField(verbose_name=_('Codeforces contest number'))
    cf_index = models.CharField(verbose_name=_('Codeforces problem index'), max_length=16)
    max_score = models.FloatField(verbose_name=_('Maximum amount of points'))