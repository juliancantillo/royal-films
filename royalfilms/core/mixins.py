# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class BaseModelMixin(models.Model):
    """
    Description: Model Description
    """

    uuid = models.UUIDField(default=uuid.uuid4, editable=False,
                            unique=True, db_index=True)

    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name=_('Created at'))

    updated_at = models.DateTimeField(auto_now=True,
    	verbose_name=_('Updated at'))

    class Meta:
       abstract = True