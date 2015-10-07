from django.db import models
from django.db.models import F
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from codeforce_it.apps.codeforces_wrapper.models import Contestant


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class Contest(models.Model):
    start_time = models.DateTimeField(_('Start time'))
    duration = models.DurationField(_('Duration'))
    contestants = models.ManyToManyField(Contestant, blank=True)

    class Meta:
        app_label = 'codeforces_wrapper'

    def __str__(self):
        return "#{}, starts at {}, ends at {}".format(self.id, self.start_time, self.end_time)

    @property
    def end_time(self):
        return self.start_time + self.duration

    @property
    def is_running(self):
        return self.start_time <= now() <= self.end_time

    @staticmethod
    def get_running_contests():
        return Contest.objects.filter(start_time__lte=now(), start_time__gte=now() - F('duration'))
