from django.contrib import admin
from .models import Album, Track


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'artist')


class TrackAdmin(admin.ModelAdmin):
    list_display = ('album', 'order', 'title', 'duration')
    def get_album(self, obj):
        return obj.album.album_name
    def get_artist(self, obj):
        return obj.album.artist






# Register your models here.
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
