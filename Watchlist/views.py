from .form import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy



def index(request): 
    return render(request,"Watchlist/index.html")

def currentlyWatching(request): 
    context = {}
    return render(request,"Watchlist/currentlyWatching.html")

def recommendations(request): 
    context = {}
    return render(request,"Watchlist/recommendations.html")

def home(request):
    context = {}
    return render(request,"Watchlist/home.html")

def login(request): 
    context = {}
    return render(request,"Watchlist/registration/login.html")

def future(request): 
    context = {}
    return render(request,"Watchlist/future.html")

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

