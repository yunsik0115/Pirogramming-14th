from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin)
    list_display = ('id','title','modified_at')
    list_filter = ('modified_at',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}

# Register your models here.
