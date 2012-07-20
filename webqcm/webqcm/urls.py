from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webqcm.views.home', name='home'),
    # url(r'^webqcm/', include('webqcm.foo.urls')),
    url(r'^associate/', include('associate.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
     from django.views.static import serve
     _media_url = settings.MEDIA_URL
     print _media_url
     if _media_url.startswith('/'):
         _media_url = _media_url[1:]
         urlpatterns += patterns('',
                                 (r'^%s(?P<path>.*)$' % _media_url,
                                 serve,
                                 {'document_root': settings.MEDIA_ROOT}))
     del(_media_url, serve)
