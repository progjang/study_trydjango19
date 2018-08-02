from django.contrib import admin
from .models import Post
# Register your models here.

class PostsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', 'created_at']
    list_display_links = ['created_at']
    list_filter = ['updated_at', 'created_at']
    search_fields = ['title', 'content']
    list_editable = ['title']
    class Meta:
        model = Post
        
admin.site.register(Post, PostsModelAdmin)

