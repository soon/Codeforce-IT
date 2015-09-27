from rest_framework import serializers

from codeforce_it.apps.codeforces_wrapper.models import Problem


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Problem
        fields = ('cf_contest_id', 'cf_index', 'max_score', 'contest')
