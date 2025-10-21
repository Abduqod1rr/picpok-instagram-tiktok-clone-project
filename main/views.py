from django.shortcuts import render, HttpResponse 
from django.views.generic import CreateView , ListView ,UpdateView ,DeleteView    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegister(UserCreationForm,CreateView):
        fields =  ['username', 'password1', 'password2']
        template_name='register.html'
        model=User
        
