from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path(
        '<int:pk>/delete_post/', BlogDeleteView.as_view(), name='delete_post'
        ),
    path('<int:pk>/edit_post/', BlogUpdateView.as_view(), name='edit_post'),
    path('add_post/', BlogCreateView.as_view(), name='add_post'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path('', BlogListView.as_view(), name='blog'),
]
