from django_cron import CronJobLog
from rest_framework import viewsets

from codeforce_it.apps.codeforces_wrapper.serializers import CronJobLogSerializer


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class CronJobLogViewSet(viewsets.ModelViewSet):
    queryset = CronJobLog.objects.all()
    serializer_class = CronJobLogSerializer
