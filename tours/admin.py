from django.contrib import admin
from .models import *

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Keyword)
admin.site.register(Tour)
admin.site.register(Stop)
admin.site.register(Block)