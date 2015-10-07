from django.contrib.auth.models import Group
from rest_framework import viewsets

from codeforce_it.apps.codeforces_wrapper.serializers import GroupSerializer


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
