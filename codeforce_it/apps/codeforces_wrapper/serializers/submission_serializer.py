from rest_framework import serializers

from codeforce_it.apps.codeforces_wrapper.models import Submission


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        fields = ('cf_id', 'problem', 'author', 'creation_time', 'verdict')
