from django.shortcuts import render
from django.views.generic import ListView

from django.contrib.gis.geoip2 import GeoIP2

from royalfilms.movies.models import Movie
from royalfilms.cinemas.models import Function, Cinema

class HomeView(ListView):
    model = Function
    template_name = "pages/home.html"

    def get_queryset(self):
        return self.model.now_playing.distinct('movie__title')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        try:
            g = GeoIP2()
            ip = self.request.META.get('REMOTE_ADDR', None)

            context['city'] = g.city(ip)['city']

        except Exception as e:
            pass

        context['cinemas'] = Cinema.objects.all()

        return context
