from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

class FunctionsManager(models.Manager):
    """
    Description: Functions model manager
    """
    def get_queryset(self):
        return super(FunctionsManager, self).get_queryset().filter(published_until__gte=timezone.now())
