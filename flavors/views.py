from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import datetime
from django.views import generic

from .models import Flavor

def index(request):
    now = datetime.datetime.now().strftime("%H:%M:%S (MSK)")
    html = "<html><body>Time: %s</body></html>" % (now)

    # return HttpResponse(html)
    return render(request, "flavors/index.html", {"data": now})
    # return render_to_response("flavors/index.html", {"data": now})

class DisplayData(generic.ListView):
    template_name = 'flavors/displaydata.html'
    context_object_name = 'data_list'

#    def get_all_flavors(self):
    def get_queryset(self):
        return Flavor.objects.order_by('title')
        # return Flavor.objects.filter(Flavor.tested==True).order_by('title')
