from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "beforelogin/index.html")

def login(request):
    return render(request, "beforelogin/login.html")

def signup(request):
    return render(request, "beforelogin/signup.html")