# blog/admin.py

from django.contrib import admin
from .models import Post

#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'updated']
    search_fields = ['title', 'content']
    list_filter = ['created']

admin.site.register(Post, PostAdmin)
