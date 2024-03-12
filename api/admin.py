from django.contrib import admin
from .models import PixelCoin, PhotoPair, Vote

# Register your models here.
admin.site.register(PixelCoin)
admin.site.register(PhotoPair)
admin.site.register(Vote)