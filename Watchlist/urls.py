from django.urls import path
import Watchlist.views

urlpatterns = [path("", Watchlist.views.index, name="index"), 
]




