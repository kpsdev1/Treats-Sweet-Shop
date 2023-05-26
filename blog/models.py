from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, ) 
    posted_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True,)

    class Meta:
        ordering = ('-posted_on',)

    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse("post_detail", kwargs={"pk": self.pk})