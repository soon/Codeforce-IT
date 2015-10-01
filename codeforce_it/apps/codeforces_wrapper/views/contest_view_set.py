from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from codeforce_it.apps.codeforces_wrapper.internal.ranklist_row import RanklistRow
from codeforce_it.apps.codeforces_wrapper.models import Contest
from codeforce_it.apps.codeforces_wrapper.serializers import ContestSerializer
from codeforce_it.apps.codeforces_wrapper.serializers.ranklist_row_serializer import RanklistRowSerializer


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @detail_route(methods=['get'])
    def standings(self, request, pk=None):
        contest = self.get_object()
        ranklist_rows = sorted(map(lambda contestant: RanklistRow.from_contest_problems(contest, contestant),
                                   contest.contestants.all()),
                               key=lambda row: row.total_score, reverse=True)
        return Response(RanklistRowSerializer(ranklist_rows, many=True).data)
