from django.shortcuts import render
from django.views.generic import ListView

from royalfilms.movies.models import Movie
from royalfilms.cinemas.models import Function, Cinema

class HomeView(ListView):
    model = Function
    template_name = "pages/home.html"

    def get_queryset(self):
        return self.model.now_playing.distinct('movie__title')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['cinemas'] = Cinema.objects.all()

        return context
