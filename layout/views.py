from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Person, Post, Follow_People
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
            User.objects.create_user(username, email, password)
            person = Person.objects.create(username=username, name=name, email=email)
            person.save()
            p = Person.objects.get(username=username)
            Follow_People.objects.create(uname=p)
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
    posts = Post.objects.all().order_by('-time')
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
    posts = Post.objects.filter(username=user).order_by('-time')
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
    if request.method=="POST":
        user = request.POST["username"]
        person = Person.objects.get(username=user)
        tag = "0"
        u = request.user.username
        if Follow_People.objects.filter(uname=u).exists():
            people = Follow_People.objects.get(uname=u)
            peo = people.to_follow.all()
            print(peo)
            for p in peo:
                if p.username==user:
                    print("exists")
                    tag = "1"
        return render(request, "afterlogin/findprofile.html", {
            "person":person,
            "tag":tag
        })
    else:
        return redirect(reverse(following))
    

@login_required
def following(request):
    if request.method=="POST":
        to_follow = request.POST["follow"]
        user = request.user.username
        person = Person.objects.get(username = user)
        to_follow_people = Person.objects.get(username = to_follow)
        if Follow_People.objects.filter(uname=person).exists():
           p = Follow_People.objects.get(uname=person)
        else:
            p = Follow_People.objects.create(uname = person)
        p.to_follow.add(to_follow_people)
        p = Follow_People.objects.get(uname = person)
        people = p.to_follow.all()
        return render(request, "afterlogin/following.html", {
            "people":people
        })
    user = request.user.username
    person = Person.objects.get(username = user)
    p = Follow_People.objects.get(uname = person)
    people = p.to_follow.all()
    return render(request, "afterlogin/following.html", {
        "people":people
    })

@login_required
def friend(request):
    if request.method=="POST":
        friend = request.POST["friend"]
        person = Person.objects.get(username=friend)
        posts = Post.objects.filter(username=person).order_by('-time')
        return render(request, "afterlogin/friend.html", {
            "person":person,
            "posts":posts
        })
    return redirect(reverse(following))

@login_required
def unfollow(request):
    if request.method=="POST":
        user_to_unfollow = request.POST["unfollow"]
        user = request.user.username
        person = Person.objects.get(username=user)
        to_unfollow = Person.objects.get(username=user_to_unfollow)
        p = Follow_People.objects.get(uname = person)
        p.to_follow.remove(to_unfollow)
        return redirect(reverse(findProfile))
    return redirect(reverse(find))


@login_required
def about(request):
    return render(request, "afterlogin/about.html")