from django.contrib import admin
from photo.models import Album, Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline, )
    list_display = ('id', 'name', 'description')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_at')

# Register your models here.
