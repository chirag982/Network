from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Person, Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse(home))
        else:
            return render(request, 'beforelogin/login.html', {
                "message": "Wrong Credentials."
            }) 
    return render(request, "beforelogin/login.html")

def index(request):
    return redirect(login_view)

def signup(request):
    if request.method=="POST":
        username = request.POST["username"]
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        if (User.objects.filter(username=username).exists()):
            return render(request, 'beforelogin/signup.html', {
                "message": "User already exists with this username"
            })
        else:
            user = User.objects.create_user(username, email, password)
            person = Person.objects.create(username=username, name=name, email=email)
            person.save()
            u = authenticate(request, username=username, password=password)
            login(request, u)
            return redirect(reverse(home), {
                "message":"User logined!"
            })
    else:
        return render(request, "beforelogin/signup.html")

@login_required    
def logout_view(request):
    logout(request)
    return redirect(index)

@login_required
def home(request):
    posts = Post.objects.all()
    return render(request, "afterlogin/home.html", {
        "posts":posts
    })

@login_required
def profile(request):
    username = request.user.username
    person = Person.objects.get(username=username)
    if request.method == "POST":
        return render(request, "afterlogin/edit.html", {
            "person":person
        })
    return render(request, "afterlogin/profile.html", {
        "person":person
    })

@login_required
def update(request):
    if request.method == "POST":
        username = request.user.username
        person = Person.objects.get(username=username)
        person.name = request.POST["name"]
        person.bio = request.POST["bio"]
        person.DOB = request.POST["dob"]
        image = request.FILES.get("image", None)
        if image:
            person.image = image
        person.save()
        return redirect(reverse(profile))

@login_required
def addpost(request):
    if request.method=="POST":
        image = request.FILES.get("image", None)
        if image:
            image = image
        content = request.POST["post"]
        user = request.user.username
        person = Person.objects.get(username=user)
        p = Post.objects.create(username = person, content=content, image=image)
        return render(request, "afterlogin/addpost.html", {
            "message":"Posted successfully!"
        })
    return render(request, "afterlogin/addpost.html")

@login_required
def mypost(request):
    user = request.user.username
    posts = Post.objects.filter(username=user)
    return render(request, "afterlogin/myposts.html", {
        "posts":posts
    })

@login_required
def find(request):
    if request.method=="POST":
        username = request.POST["username"]
        if Person.objects.filter(username=username):
            person = Person.objects.get(username=username)
            return render(request, "afterlogin/find.html", {
                "person":person
            })
        return render(request, "afterlogin/find.html", {
            "message":f"Oops! Not found anybody with this username-{username}..."
        })
    return render(request, "afterlogin/find.html")

@login_required
def findProfile(request):
    return render(request, "afterlogin/findprofile.html")
    

@login_required
def following(request):
    return render(request, "afterlogin/following.html")

@login_required
def about(request):
    return render(request, "afterlogin/about.html")