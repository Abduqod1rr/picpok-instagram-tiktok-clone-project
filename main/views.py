from django.shortcuts import render, HttpResponse 
from django.views.generic import CreateView , ListView ,UpdateView ,DeleteView    
from django.contrib.auth.forms import UserCreationForm

class UserRegister(UserCreationForm,CreateView):
        fields=['username','password']
        template_name='register.html'
        