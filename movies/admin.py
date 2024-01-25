from django.contrib import admin
from .models import Genre, Movie
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class MovieAdmin(admin.ModelAdmin):
    fields = ("title","release_year", "number_in_stock", "daily_rate", "genre")
    list_display = ("title", "number_in_stock", "daily_rate")
    
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
