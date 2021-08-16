from django.contrib import admin
from .models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=('name','year','star','show')
    list_filter=('star','show')
admin.site.register(Movie,MovieAdmin)