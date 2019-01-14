from django.contrib import admin
from .models import Post, Tag



class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'summary', 'created_date', 'published_date')
    list_filter = ['created_date', 'published_date', 'tag']

admin.site.register(Post, PostAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tag, TagAdmin)