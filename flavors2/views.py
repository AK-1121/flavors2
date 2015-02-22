from django.shortcuts import render
from django.views.generic import ListView

from .models import FlavorReview

class TestFlavor2(ListView):
    template_name = "flavors2/results.html"
    context_object_name = 'data_list'

    def get_queryset(self):
        return FlavorReview.objects.all()#.values()

