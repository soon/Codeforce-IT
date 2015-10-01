from rest_framework import serializers

from codeforce_it.apps.codeforces_wrapper.serializers import ContestantSerializer, ProblemResultSerializer


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class RanklistRowSerializer(serializers.Serializer):
    contestant = ContestantSerializer()
    problem_results = ProblemResultSerializer(many=True)
    total_score = serializers.FloatField()
