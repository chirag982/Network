from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect(login)

def login(request):
    if request.method=="POST":
        pass
    else:
        return render(request, "beforelogin/login.html")

def signup(request):
    if request.method=="POST":
        pass
    else:
        return render(request, "beforelogin/signup.html")
    
def home(request):
    return render(request, "afterlogin/home.html")

def profile(request):
    return render(request, "afterlogin/profile.html")

def addpost(request):
    return render(request, "afterlogin/addpost.html")

def find(request):
    return render(request, "afterlogin/find.html")

def following(request):
    return render(request, "afterlogin/following.html")

def about(request):
    return render(request, "afterlogin/about.html")