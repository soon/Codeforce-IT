from django.contrib.auth.models import Group
from rest_framework import serializers


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
