from .models import Post, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    """Reviews Form"""
    class Meta:
        model = Post
        fields = ('title', 'body', 'image')

        widgets = {
            'body': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    """Comment Form"""
    class Meta:
        model = Comment
        fields = ('comment',)
