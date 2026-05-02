from django.contrib import admin
from .models import Post, Author, Comment

# Register your models here.
class CommentInLine(admin.TabularInline):
    model = Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]
    
admin.site.register(Author)
admin.site.register(Comment)