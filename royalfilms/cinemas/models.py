from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from royalfilms.core.mixins import BaseModelMixin
from royalfilms.movies.models import Movie

class Cinema(BaseModelMixin):
    """
    Description: Cinema Model
    """

    name = models.CharField(max_length=255, blank=False,
    	verbose_name=_('Name'))

    address = models.CharField(max_length=255, blank=False,
    	verbose_name=_('Address'))


    functions = models.ManyToManyField(
		Movie,
        through='Function',
        through_fields=('cinema', 'movie'),
    	)


    lat = models.FloatField(default=0.0,
    	verbose_name=_('Latitude'))

    lng = models.FloatField(default=0.0,
    	verbose_name=_('Longitude'))

    def __str__(self):
    	return self.name

    def __unicode__(self):
        return self.name



class Function(BaseModelMixin):
    """
    Description: Movies functions in a Cinema
    """
    cinema = models.ForeignKey(Cinema)

    movie = models.ForeignKey(Movie)

    published_at = models.DateField(
        auto_now_add=True,
        verbose_name=_('Published at'))

    published_until = models.DateField(
        blank=False,
        verbose_name=_('Published until'))

    def __str__(self):
        return _('{1} in {0}').format(self.cinema.name, self.movie.title)

    def __unicode__(self):
        return _('{1} in {0}').format(self.cinema.name, self.movie.title)


class Show(BaseModelMixin):
    """
    Description: Show model
    """
    time = models.TimeField(auto_now=False, blank=False)

    #sell_until, show_date, is_available_for_sale, is_sold_out, prices

    function = models.ForeignKey(Function)

    def __str__(self):
        return _('{0} in {1} at {2}').format(
            self.function.movie.title,
            self.function.cinema.name,
            self.time)

    def __unicode__(self):
        return _('{0} in {1} at {2}').format(
            self.function.movie.title,
            self.function.cinema.name,
            self.time)




