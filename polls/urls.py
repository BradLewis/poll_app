#url file for django
from django.conf.urls import url

from . import views

urlpatterns = [
    # eg: /polls/
    url(r'^$', views.index, name='index'),
    # eg: /polls/10/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # eg: /polls/10/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #eg: /polls/10/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
