from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from .models import Cinema, Function, Show, Auditorium, FunctionType

@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_filter = ('city',)
    list_display = ('name', 'city',)


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_filter = ('cinema__name','published_until','movie')

    def get_queryset(self,request):
        return self.model.objects.all()

@admin.register(FunctionType)
class FunctionTypeAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'function','is_3D')
    list_filter = ('function__cinema__name','function__movie')
    pass

@admin.register(Auditorium)
class AuditoriumAdmin(admin.ModelAdmin):
    list_filter = ('cinema__name','cinema__city',)
    pass

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_filter = ('function_type__auditorium__cinema','function_type__function__movie')
    pass
