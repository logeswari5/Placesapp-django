from django.db import models

from django.contrib.gis.db import models
# from django.db import models


class PlaceType(models.Model):
    place_type = models.CharField(max_length=200, help_text="Enter place type")

    def __str__(self):
        return self.place_type


class Place(models.Model):
    title = models.CharField(max_length=200)
    location = models.PointField()
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    city = models.CharField(max_length=100)
    type_of_place = models.ForeignKey('PlaceType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    @property
    def lat_lon(self):
        return list(getattr(self.location, 'coords', [])[::-1])


