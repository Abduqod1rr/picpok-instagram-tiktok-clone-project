from django.shortcuts import render, HttpResponse 
from django.views.generic import CreateView , ListView ,UpdateView ,DeleteView    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import forms

class UserRegister(CreateView):
        form_class=forms.cutomuserform
        template_name='register.html'
        model=User
        
