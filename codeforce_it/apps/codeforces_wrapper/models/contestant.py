from django.db import models
from django.utils.translation import ugettext_lazy as _


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class Contestant(models.Model):
    cf_handle = models.CharField(verbose_name=_('Codeforces Handle'), max_length=64)
