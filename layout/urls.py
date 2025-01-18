from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"), 
    path("login/", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("new-post", views.addpost, name="addpost"),
    path("find/", views.find, name="find"),
    path("about/", views.about, name="about"),
]