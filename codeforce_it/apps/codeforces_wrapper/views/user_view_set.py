from django.contrib.auth.models import User
from rest_framework import viewsets

from codeforce_it.apps.codeforces_wrapper.serializers import UserSerializer


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
