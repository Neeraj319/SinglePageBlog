from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE , blank=True , null=True)
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    like = models.ManyToManyField(
        User, related_name='like', blank=True)

    def __str__(self):
        return f'{self.blog.title}'
