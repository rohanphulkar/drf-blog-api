from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from user.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100,default='')
    image = models.ImageField(upload_to='django_blog_api/post/', blank=True)
    content = RichTextField()
    slug = AutoSlugField(populate_from='title')
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.comment