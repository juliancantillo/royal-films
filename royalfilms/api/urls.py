# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from rest_framework import routers

from royalfilms.movies import api as movies
from royalfilms.cinemas import api as cinemas


router = routers.SimpleRouter()
router.register(r'movies', movies.MovieViewSet)
router.register(r'cinemas', cinemas.CinemaViewSet)


urlpatterns = [

    url(
        regex=r'^showtimes/(?P<uuid>[-\w]+)/$',
        view=cinemas.ShowtimesView.as_view(),
        name='showtimes'
    ),
] + router.urls
