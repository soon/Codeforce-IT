from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from codeforce_it.apps.codeforces_wrapper.models import Contestant
from codeforce_it.apps.codeforces_wrapper.serializers import ContestantSerializer


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class ContestantViewSet(viewsets.ModelViewSet):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
