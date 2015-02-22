from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj_site03.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^flavors/', include('flavors.urls')),
    url(r'^flavors2/', include('flavors2.urls')),
    # url(r'^polls/', include('polls.urls', namespace="polls")),
)
