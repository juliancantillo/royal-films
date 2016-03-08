from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from .models import Cinema, Function, Show

@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    pass


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_filter = ('cinema__name','published_until',)

    def get_queryset(self,request):
        return self.model.objects.all()

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    pass
