from rest_framework import serializers

from codeforce_it.apps.codeforces_wrapper.serializers import ContestantSerializer
from codeforce_it.apps.codeforces_wrapper.serializers.problem_result_serializer import ProblemResultSerializer


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class RanklistRowSerializer(serializers.Serializer):
    contestant = ContestantSerializer()
    problem_results = ProblemResultSerializer(many=True)
    total_score = serializers.FloatField()
