from django.conf import settings
from django.db import models
from django.utils import timezone

# MODELS for MTM Tours app

class Tour(models.Model):
    # name = CharField  # Long name
    # name_short = CharField  # Short name
    # slug = SlugField  # Slug (for URLs)
    # start_location = ForeignKey  # Location (name, gps coords, maybe more) in a separate model - DRY
    # categories = ManyToMany  # Categories of the Tour (Many-To-Many relationship)
    # description = TextField  # Tour Description
    # length = DecimalField  # Tour length in hours
    pass

class Stop(models.Model):
    # name
    # tour
    # location
    # description
    pass

class Block(models.Model):
    # name
    # stop
    # order
    # keywords
    # text
    # audio
    pass

class Location(models.Model):
    # name
    # gps TODO: Look up GeoDjango for this bit
    # latitude
    # longitude
    pass

class Category (models.Model):
    # name
    pass