from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Movie, MovieAdmin)
