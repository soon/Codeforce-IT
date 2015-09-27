from django.contrib.auth.models import User
from rest_framework import serializers


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
