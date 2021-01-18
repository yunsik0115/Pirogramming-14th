from django.contrib import admin
from .models import Item, Item


# admin.site.register(Item)

#등록법 2
# class ItemAdmin(admin.ModelAdmin):
# pass

#등록법 3
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_published']
    list_display_links = ['name']
    search_fields = ['name'] # 기본 조건 : OR
    list_filter = ['is_published', 'updated_at']

    def short_desc(self, item):
        return item.desc[:20]