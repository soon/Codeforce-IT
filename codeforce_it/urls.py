from django.conf.urls import include, url
from rest_framework import routers

from codeforce_it.apps.codeforces_wrapper import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
