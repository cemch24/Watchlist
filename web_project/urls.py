"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from Watchlist import views
import Watchlist.urls
from Watchlist.views import SignUpView, profile
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', Watchlist.views.home, name="home"),
    path('', include("django.contrib.auth.urls")), 
    path('index/', include("Watchlist.urls")),
    path("second/", Watchlist.views.currentlyWatching, name="currentlyWatching"), 
    path("third/", Watchlist.views.recommendations, name="recommendations"),
    path("login/", Watchlist.views.login, name="login"),
    path("fifth/", Watchlist.views.future, name="future"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('profile/', profile, name='users-profile'),
    path('update/', Watchlist.views.update, name='update'),

    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
