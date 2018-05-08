# from django.urls import path
from django.conf.urls import url

from . import views

# urlpatterns = [
#     url('', views.index, name='index'),
# ]

app_name = 'polls'
urlpatterns = [
    url('', views.IndexView.as_view(), name='index'),
    url('^(?P<pk>[0-9]+)/detail/$', views.DetailView.as_view(), name='detail'),
    url('^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url('^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
