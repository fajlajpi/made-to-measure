from django.conf import settings
from django.db import models
from django.utils import timezone

# MODELS for MTM Tours app

class Location(models.Model):
    # gps TODO: Look up GeoDjango for this bit
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(decimal_places=6, max_digits=9)
    longitude = models.DecimalField(decimal_places=6, max_digits=9)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Keyword(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tour(models.Model):
    name = models.CharField(max_length=200)
    name_short = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    start_location = models.ForeignKey(Location, on_delete=models.PROTECT)
    categories = models.ManyToManyField(Category)
    description = models.TextField()
    length = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return self.name_short

class Stop(models.Model):
    name = models.CharField(max_length=200)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField
    order = models.SmallIntegerField()

    def __str__(self):
        return self.name

class Block(models.Model):
    name = models.CharField(max_length=200)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()
    keywords = models.ManyToManyField(Keyword)
    skippable = models.BooleanField(default=True)
    text = models.TextField()
    # audio TODO: Look up how to upload sound clips to blocks and construct the tour out of them

    def __str__(self):
        return self.name