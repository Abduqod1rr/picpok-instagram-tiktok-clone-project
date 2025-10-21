from django.urls import path
from . import views

urlpatterns = [
     #paths
    path("register", views.UserRegister.as_view(), name="register")
]
