from django.contrib import admin

from .models import Genre,Movies

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class MoviesAdmin(admin.ModelAdmin):

    exclude = ('date_created',)
    list_display = ('title','number_in_stock','genre')
admin.site.register(Genre)
admin.site.register(Movies,MoviesAdmin)


