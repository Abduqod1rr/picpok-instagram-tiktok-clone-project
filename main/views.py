from django.shortcuts import render, HttpResponse 
from django.views.generic import CreateView , ListView ,UpdateView ,DeleteView    
    # Create your views here.

def hello1func(request):

    return HttpResponse("hello it's the picpok project i'm making docs and readme")


