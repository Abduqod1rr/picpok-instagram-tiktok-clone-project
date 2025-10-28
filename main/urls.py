from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     #paths
    path("register/", views.UserRegister.as_view(), name="register"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", views.userlogout.as_view(), name="logout"),
    path("createprofile", views.CreateProfile.as_view(), name="createprofile"),
    path("", views.Home.as_view(), name="home"),
    path("addpoc/", views.AddPoc.as_view(), name="addpoc"),
    path("mypocs/", views.MyPocs.as_view(), name="mypocs"),
    path("delete_poc/<int:pk>", views.DeletePoc.as_view(), name="delete_poc"),
    path("update_poc/<int:pk>",views.UpdatePoc.as_view(), name='update_poc'),
    path("myprofile/", views.MyProfile.as_view(), name="myprofile"),
    path("edit_profile/", views.EditProfile.as_view(), name="edit_profile")
     #
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
