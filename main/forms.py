from django import forms
from django.contrib.auth.models import User

class cutomuserform(forms.ModelForm):
    class Meta:
        model= User
        feilds=['username','password1','password2']