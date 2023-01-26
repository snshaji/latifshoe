from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style ="border-radius: 50px" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car image'
    list_display = ('id','thumbnail','car_title','color','model','year','is_featured')
    list_display_links = ('id','thumbnail')
    list_editable = ('is_featured',)
    search_fields = ('id','thumbnail','car_title',)
    list_filter = ('car_title','model')
admin.site.register(Car,CarAdmin)
