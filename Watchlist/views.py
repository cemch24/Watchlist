from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm



def index(request): 
    return render(request,"Watchlist/index.html")

def currentlyWatching(request): 
    context = {}
    return render(request,"Watchlist/currentlyWatching.html")

def recommendations(request): 
    context = {}
    return render(request,"Watchlist/recommendations.html")

def login(request): 
    context = {}
    return render(request,"Watchlist/login.html")

def home(request): 
    context = {}
    return render(request,"Watchlist/home.html")

