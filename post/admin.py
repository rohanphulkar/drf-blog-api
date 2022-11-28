from django.contrib import admin
from .models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display=['title','slug','date']
admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display=['comment','post']
admin.site.register(Comment,CommentAdmin)