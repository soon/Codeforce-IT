from rest_framework import serializers


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class ProblemResultSerializer(serializers.Serializer):
    points = serializers.FloatField(min_value=0)
    rejected_attempt_count = serializers.IntegerField(min_value=0)
    best_submission_time = serializers.IntegerField(min_value=0)
