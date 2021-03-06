from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # choices for the category of the blog
    an_type = (
        ("Fashion", "Fashion "),
        ("Food", "Food"),
        ("Travel", "Travel"),
        ("Music", "Music"),
        ("Lifestyle", "Lifestyle"),
        ("Fitness", "Fitness"),
        ("DIY", "DIY"),
        ("Sports", "Sports"),
        ("Political", "Political"),
        ("Tech", "Tech"),
        ("Gaming", "Gaming"),
        ("Pet", "Pet"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=50, choices=an_type, default=None, blank=True, null=True
    )
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    comment model for the blog model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    like = models.ManyToManyField(User, related_name="like", blank=True)

    def __str__(self):
        return f"{self.blog.title}"
