from django.shortcuts import render, HttpResponse 
from django.views.generic import CreateView , ListView ,UpdateView ,DeleteView    , DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import forms
from django.contrib.auth.views import LoginView , LogoutView
from django.urls import reverse_lazy
from .models import Poc ,Profile ,Comment

class UserRegister(CreateView):
        form_class=forms.cutomuserform
        template_name='register.html'
        model=User
        success_url= reverse_lazy('login')

class UserLogin(LoginView):
        template_name='login.html'
        success_url=reverse_lazy('register')

class userlogout(LogoutView):
       success_url=reverse_lazy('login')

class CreateProfile(CreateView):
        model=Profile
        fields=['bio','picture']
        template_name='createprofile.html'
        success_url=reverse_lazy('login')

        def form_valid(self, form):
            form.instance.user=self.request.user
            return super().form_valid(form)
        
class Home(ListView):
       model=Poc
       template_name='home.html'

      
class AddPoc(CreateView):
       model=Poc
       fields=['title','content']
       template_name='addpoc.html'
       success_url=reverse_lazy('home')

       def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
       
class MyPocs(ListView):
      model=Poc 
 #i'll add template

      def get_queryset(self):
          return Poc.objects.filter(owner=self.request.user)
