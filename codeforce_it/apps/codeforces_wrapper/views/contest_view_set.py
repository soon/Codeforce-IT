from rest_framework import viewsets

from codeforce_it.apps.codeforces_wrapper.models import Contest
from codeforce_it.apps.codeforces_wrapper.serializers import ContestSerializer


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
