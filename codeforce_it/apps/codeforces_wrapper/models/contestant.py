from django.db import models
from django.utils.translation import ugettext_lazy as _


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class Contestant(models.Model):
    cf_handle = models.CharField(verbose_name=_('Codeforces Handle'), max_length=64)

    class Meta:
        app_label = 'codeforces_wrapper'

    def __str__(self):
        return self.cf_handle

    @property
    def codeforces_url(self):
        return 'http://codeforces.com/profile/{}'.format(self.cf_handle)
