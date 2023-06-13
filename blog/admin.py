from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = [
        "title",
        "posted_on",
    ]
    summernote_fieds = ('body')


admin.site.register(Post, BlogAdmin)
admin.site.register(Comment)
