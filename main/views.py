from django.shortcuts import render, HttpResponse 
from django.views.generic import CreateView , ListView ,UpdateView ,DeleteView    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import forms
from django.contrib.auth.views import LoginView , LogoutView
from django.urls import reverse_lazy

class UserRegister(CreateView):
        form_class=forms.cutomuserform
        template_name='register.html'
        model=User
        success_url= reverse_lazy('login')

class UserLogin(LoginView):
        template_name='login.html'
        success_url=reverse_lazy('register')