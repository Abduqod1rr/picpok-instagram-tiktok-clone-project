from django.urls import path
from . import views

urlpatterns = [
     #paths
    path("register/", views.UserRegister.as_view(), name="register"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("create-profile/", views.CreateProfile.as_view(), name="createprofile")
]
