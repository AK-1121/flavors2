import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView

from .models import FlavorReview

class TestFlavor2(ListView):
    template_name = "flavors2/results.html"
    context_object_name = 'data_list'

    def get_queryset(self):
        return FlavorReview.objects.all()#.values()

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse('')
        response['Last-Modified'] = last_book.publication_date.strftime(
                                    '%a, %d %b %Y %H:%M:%S GMT')
        return response

def methods(request):
    now = datetime.datetime.now()
    data = {"Request": str(dir(request)),
            "COOKIES": str(request.COOKIES),
            "REQUEST": str(request.REQUEST),
            "GET": str(request.GET),
            "FILES": str(request.FILES),
            "META": str(request.META),
            'test': 'test123'
    }

    #return HttpResponse(html)
    return render(request, "flavors2/test_methods.html", {"data_dict": data})
