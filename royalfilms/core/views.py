from django.shortcuts import render
from django.views.generic import ListView

from ipware.ip import get_real_ip
from geoip2.errors import AddressNotFoundError
from django.contrib.gis.geoip2 import GeoIP2
from django.utils.translation import ugettext_lazy as _

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
            ip = get_real_ip(self.request)

            context['city'] = g.city(ip)['city']

        except AddressNotFoundError as e:
            context['city'] = _('Unknown')

        context['cinemas'] = Cinema.objects.all()

        return context
