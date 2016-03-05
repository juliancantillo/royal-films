# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from royalfilms.movies import views as movies

urlpatterns = [

    url(
    	regex=r'^(?P<slug>[-\w]+)/$', 
    	view=movies.MovieDetailView.as_view(), 
    	name='detail'
    ),
]