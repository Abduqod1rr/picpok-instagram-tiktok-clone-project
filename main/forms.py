from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class cutomuserform(UserCreationForm):
    class Meta:
        model= User
        feilds=['username','password1','password2']