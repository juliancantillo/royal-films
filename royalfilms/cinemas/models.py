from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from .managers import FunctionsManager

from royalfilms.core.mixins import BaseModelMixin
from royalfilms.core import constants
from royalfilms.movies.models import Movie

class Cinema(BaseModelMixin):
    """
    Description: Cinema Model
    """

    name = models.CharField(max_length=255, blank=False,
    	verbose_name=_('Name'))

    address = models.CharField(max_length=255, blank=False,
    	verbose_name=_('Address'))

    phone = models.CharField(max_length=25, blank=True,
        verbose_name=_('Phone'))

    city = models.CharField(max_length=50, blank=True,
        choices=constants.CITIES, verbose_name=_('City'))


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

    showtimes = models.ManyToManyField(
        'Auditorium',
        through='FunctionType',
        through_fields=('function', 'auditorium'),
        )

    now_playing = FunctionsManager()
    objects = models.Manager()


    def __str__(self):
        return _('{1} in {0}').format(self.cinema.name, self.movie.title)

    def __unicode__(self):
        return _('{1} in {0}').format(self.cinema.name, self.movie.title)


class FunctionType(models.Model):
    """
    Description: Function type
    """
    function = models.ForeignKey('Function')
    auditorium = models.ForeignKey('Auditorium',null=True)

    is_3D = models.BooleanField(default=False,
        verbose_name=_('Is 3D'))

    def __str__(self):
        return _('{0} in Auditorium {1}').format(self.function, self.auditorium.name)

    def __unicode__(self):
        return _('{0} in Auditorium {1}').format(self.function, self.auditorium.name)


class Auditorium(models.Model):
    """
    Description: Function Auditorium
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False,
                            unique=True, db_index=True)

    name = models.CharField(max_length=100, blank=False,
        verbose_name=_('Name'))

    cinema = models.ForeignKey(Cinema)


    def __str__(self):
        return _('Auditorium {1} in {0}').format(self.cinema.name, self.name)

    def __unicode__(self):
        return _('Auditorium {1} in {0}').format(self.cinema.name, self.name)


class Show(BaseModelMixin):
    """
    Description: Show model
    """
    time = models.TimeField(auto_now=False, blank=False)
    function_type = models.ForeignKey('FunctionType',null=True)
    booking_url = models.URLField(blank=True,
        verbose_name=_('Booking URL'))
    #TODO
    #sell_until, show_date, is_available_for_sale, is_sold_out, prices


    def __str__(self):
        return _('{0} at {1}').format(self.function_type, self.time)

    def __unicode__(self):
        return _('{0} at {1}').format(self.function_type, self.time)




