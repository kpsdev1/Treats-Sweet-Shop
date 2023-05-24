from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('add_review/', ReviewCreateView.as_view(), name='add_review'),
    path('', views.ReviewsList.as_view(), name='reviews'),
]