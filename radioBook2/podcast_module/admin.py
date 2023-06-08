from django.contrib import admin
from podcast_module import models

# Register your models here.


admin.site.register(models.Tag)
admin.site.register(models.Season)
admin.site.register(models.Podcast)
