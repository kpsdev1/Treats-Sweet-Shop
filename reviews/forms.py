from .models import Review
from django import forms



class ReviewForm(forms.ModelForm):
    """Reviews Form"""
    class Meta:
        model = Review
        fields = ('title', 'body', 'rating')