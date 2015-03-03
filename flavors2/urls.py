from django.conf.urls import patterns
from django.conf.urls import url, include

from flavors2 import views

urlpatterns = patterns('',
    url(r"^$", views.TestFlavor2.as_view(), name="index2"),
    url(r'^login/$', 'django.contrib.auth.views.login', 
        {'template_name': 'flavors2/login1.html'}
    ),

    url(r'^methods/$', views.methods),

)

