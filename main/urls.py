from django.urls import path
from . import views

urlpatterns = [
    #paths
    path("", views.hello1func, name="sa")
]
