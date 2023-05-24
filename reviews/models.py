from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.
STARS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class Review(models.Model):
    """This is the model for wine"""
    title = models.CharField(max_length=120, blank=False)
    rating = models.CharField(
        max_length=5, choices=STARS, default='5', blank=False)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review")

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reviews')