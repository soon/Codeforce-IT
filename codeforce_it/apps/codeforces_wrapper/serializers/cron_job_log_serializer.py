from rest_framework import serializers
from django_cron.models import CronJobLog


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class CronJobLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CronJobLog
        fields = ('url', 'code', 'start_time', 'end_time', 'is_success', 'message')
        read_only_fields = ('url', 'code', 'start_time', 'end_time', 'is_success', 'message')
