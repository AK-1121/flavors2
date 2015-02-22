from django.conf.urls import patterns
from django.conf.urls import url

#from flavors2.views import TasteDetailView
#from flavors2.views import TasteResultsView
from flavors2 import views

urlpatterns = patterns('',
    url(
        #regex=r"^(?P<pk>\d+)/$",
        r"^$",
        views.TestFlavor2.as_view(),
        name="detail"
    )

)

