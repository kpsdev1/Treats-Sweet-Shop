from django.contrib import admin
from .models import Review



# Register your models here.
@admin.register(Review)
class AdminForComment(admin.ModelAdmin):
    """This is for the admin to manage Wines"""
    list_filter = ('title', 'rating', 'date_added', 'posted_by')
    list_display = ('title', 'rating', 'date_added', 'posted_by')
    search_fields = ('title', 'rating', 'date_added', 'posted_by')