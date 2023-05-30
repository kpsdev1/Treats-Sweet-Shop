from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1)
    posted_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    image = models.ImageField(null=True, blank=True,)

    class Meta:
        ordering = ('-posted_on',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    """This is the model for comments"""
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=90)
    comment = models.TextField()
    email = models.EmailField()
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['posted_on']

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("article_list")
