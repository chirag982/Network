from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"), 
    path("login/", views.login_view, name="login"),
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("new-post", views.addpost, name="addpost"),
    path("myposts/", views.mypost, name="mypost"),
    path("find/", views.find, name="find"),
    path("following", views.following, name="following"),
    path("about/", views.about, name="about"),
    path("logout", views.logout_view, name="logout"),

    path("findprofile", views.findProfile, name="findprofile"),
    path("update/", views.update, name="update"),
]