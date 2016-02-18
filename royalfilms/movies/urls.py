# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

from royalfilms.movies import views as movies

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[-\w]+)/$', movies.MovieDetailView.as_view(), name='detail'),
    )