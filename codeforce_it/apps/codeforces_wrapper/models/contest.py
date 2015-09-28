from django.db import models
from django.utils.translation import ugettext_lazy as _

from codeforce_it.apps.codeforces_wrapper.models import Contestant


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class Contest(models.Model):
    start_time = models.DateTimeField(_('Start time'))
    duration = models.DurationField(_('Duration'))
    contestants = models.ManyToManyField(Contestant, blank=True)

    def __str__(self):
        return "#{}, starts at {}, ends at {}".format(self.id, self.start_time, self.end_time)

    @property
    def end_time(self):
        return self.start_time + self.duration
