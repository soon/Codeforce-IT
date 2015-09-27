from rest_framework import viewsets

from codeforce_it.apps.codeforces_wrapper.models import Problem

from codeforce_it.apps.codeforces_wrapper.serializers import ProblemSerializer


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
