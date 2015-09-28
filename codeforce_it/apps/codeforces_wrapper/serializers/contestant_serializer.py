from rest_framework import serializers

from codeforce_it.apps.codeforces_wrapper.models import Contestant


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class ContestantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contestant
        fields = ('cf_handle', 'codeforces_url')
        read_only_fields = ('codeforces_url',)
