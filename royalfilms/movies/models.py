from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField

class Movie(models.Model):
    """
    Description: Model for movies
    """
    title = models.CharField(max_length=200, verbose_name=_('Title'))

    slug = AutoSlugField(populate_from='title')

    plot = models.TextField(
        max_length=1000, blank=False,
        verbose_name=_('Plot'))
    # Movie poster for theaters
    poster = models.ImageField(upload_to='movies/covers/')

    runtime = models.IntegerField(default=0, verbose_name=_('Runtime'))
    # ID from the Internet Movie Database
    imdbID = models.CharField(max_length=55, verbose_name=_('Imdb'))
    
    imdbRating = models.FloatField(default=0.0, verbose_name=_('Imdb Rating'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.title