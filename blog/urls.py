from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
]
