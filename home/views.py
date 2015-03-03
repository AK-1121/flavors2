from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.apps import apps
from django.core.context_processors import csrf

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('home/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        #return HttpResponseRedirect('/accounts/loggedin')
        return render(request, 'home/index.html', {"user": user})
    else:
        #return HttpResponseRedirect('/accounts/invalid')
        return render(request, 'home/index.html', {"user": ""})

def index(request):
    all_apps = apps.get_models()
    list1 = [x._meta for x in all_apps]
    list2 = [x.__str__ for x in all_apps]
    list3 = [x.__dict__ for x in all_apps]
    return render_to_response('home/index.html', 
                              {'list_of_lists': [list1, list2, list3]}
                             )

# Create your views here.
