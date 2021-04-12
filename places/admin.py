from django.contrib import admin
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from places.models import Place, PlaceType

@admin.register(Place)
class PlaceAdmin(OSMGeoAdmin):
    default_lon = 1400000
    default_lat = 7495000
    default_zoom = 12
    list_display = ('title', 'location', 'city')



@admin.register(PlaceType)
class PlaceTypeAdmin(admin.ModelAdmin):
    list_display = ('place_type',)