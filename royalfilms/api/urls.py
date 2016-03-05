# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from royalfilms.movies import api as movies
from royalfilms.cinemas import api as cinemas

urlpatterns = [
    url(
    	regex=r'^movies/$', 
    	view=movies.MovieList.as_view(),
    	name='movies'
	),
	url(
    	regex=r'^cinemas/$', 
    	view=cinemas.CinemaList.as_view(),
    	name='cinemas'
	),
]