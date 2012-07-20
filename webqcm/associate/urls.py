from django.conf.urls import patterns, include, url

urlpatterns = patterns('associate.views',
    url(r'^$', 'index'),
    url(r'^(?P<copie_id>\d+)/$', 'copie'),
#    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
) 
