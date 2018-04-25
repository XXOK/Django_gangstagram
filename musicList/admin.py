from django.contrib import admin
from musicList.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'link', 'text', 'created_date',]

admin.site.register(Post, PostAdmin)