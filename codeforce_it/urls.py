from django.conf.urls import include, url
from django.views.generic import TemplateView
from rest_framework import routers

from codeforce_it.apps.codeforces_wrapper import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'problems', views.ProblemViewSet)
router.register(r'contestants', views.ContestantViewSet)
router.register(r'contests', views.ContestViewSet)
router.register(r'submissions', views.SubmissionViewSet)
router.register(r'cron-job-logs', views.CronJobLogViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^contests/\d+$', TemplateView.as_view(template_name='contest_standings.html')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
