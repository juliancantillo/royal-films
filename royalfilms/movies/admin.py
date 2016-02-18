from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass