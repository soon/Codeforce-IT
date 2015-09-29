from rest_framework import serializers

from codeforce_it.apps.codeforces_wrapper.models import Contest


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class ContestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contest
        fields = ('url', 'id', 'start_time', 'duration', 'contestants', 'end_time', 'problem_set')
        read_only_fields = ('end_time', 'problem_set')
