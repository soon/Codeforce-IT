from datetime import timedelta

from django.test import TestCase
from django.utils.timezone import now

from codeforce_it.apps.codeforces_wrapper.models import Contest


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class ContestTest(TestCase):
    def test_get_running_contests(self):
        Contest.objects.create(start_time=now() - timedelta(hours=1), duration=timedelta(hours=2))
        self.assertEquals(1, len(Contest.get_running_contests()))
