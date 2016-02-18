# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

from royalfilms.movies import api as movies

urlpatterns = patterns(
    '',
    url(r'^movies/$', movies.MovieList.as_view()),
    )