from django.urls import path
from . import views

urlpatterns = [
     #paths
    path("register/", views.UserRegister.as_view(), name="register"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", views.userlogout.as_view(), name="logout"),
    path("create-profile/", views.CreateProfile.as_view(), name="createprofile"),
    path("home/", views.Home.as_view(), name="home")
]
