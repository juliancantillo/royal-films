# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from royalfilms.core.mixins import BaseModelMixin

@python_2_unicode_compatible
class User(AbstractUser, BaseModelMixin):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Full name"), blank=True, max_length=255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'uuid': self.uuid})
