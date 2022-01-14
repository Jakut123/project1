from django.contrib import admin

from main.models import Music, Category, Comment, Favorites, Rating

admin.site.register(Music)
admin.site.register(Category)
admin.site.register(Favorites)
admin.site.register(Comment)
admin.site.register(Rating)
