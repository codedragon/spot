from django.conf.urls import patterns, url

from stats import views

urlpatterns = patterns('',
    url(r'^$', views.ListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)

