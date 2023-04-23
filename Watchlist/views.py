from .form import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .form import UserUpdateForm, ProfileUpdateForm
from .models import UserProfile



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
    return render(request,"Watchlist/login.html")

def future(request): 
    context = {}
    return render(request,"Watchlist/future.html")

def update(request): 
    context = {}
    return render(request,"registration/update.html")

def profile(request):
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.phone_number = request.POST['phone_number']
        user_profile.address = request.POST['address']
        user_profile.save()
        return redirect('profile')

    else:
        user_profile = UserProfile.objects.get(user=request.user)
        context = {'user_profile': user_profile}
        return render(request, 'profile.html', context)

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('update')
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'registration/profile.html', context)


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'email', 'bio', 'profile_picture']
    template_name = 'profile/edit.html'
    success_url = reverse_lazy('profile')

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile/detail.html'
    login_url = '/login/'

    def get_object(self, queryset=None):
        return self.request.user.profile

