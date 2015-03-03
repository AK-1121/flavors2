from django.conf.urls import patterns, url
from flavors import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index1'),
    url(r'data/$', views.DisplayData.as_view(), name="displaydata"),
)
