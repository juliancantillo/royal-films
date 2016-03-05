from django.shortcuts import render
from django.views.generic import ListView

from royalfilms.movies.models import Movie

class HomeView(ListView):
    model = Movie
    template_name = "pages/home.html"