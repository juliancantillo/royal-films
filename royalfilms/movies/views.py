from django.shortcuts import render
from django.views.generic import DetailView

from .models import Movie

class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/detail.html"