from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

import config.settings as conf
from autoslug import AutoSlugField

from royalfilms.core.mixins import BaseModelMixin


class Movie(BaseModelMixin):
    """
    Description: Model for movies
    """
    title = models.CharField(max_length=200, 
        verbose_name=_('Title'))

    original_title = models.CharField(max_length=200, 
        verbose_name=_('Original Title'), blank=True)

    slug = AutoSlugField(populate_from='title')

    synopsis = models.TextField(
        max_length=1000, blank=False,null=True,
        verbose_name=_('Synopsis'))

    plot = models.TextField(
        max_length=1000, blank=False,
        verbose_name=_('Plot'))

    # Movie poster for theaters
    poster = models.ImageField(upload_to='movies/covers/')

    horizontal_poster = models.ImageField(upload_to='movies/covers/', blank=True)

    trailer_url = models.CharField(max_length=255, 
        verbose_name=_('Trailer'), blank=True)

    runtime = models.IntegerField(default=0, 
        verbose_name=_('Runtime'))
    # ID from the Internet Movie Database
    imdbID = models.CharField(max_length=55, 
        verbose_name=_('Imdb'))
    
    imdbRating = models.FloatField(default=0.0, 
        verbose_name=_('Imdb Rating'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:detail', args=[str(self.slug)])
        