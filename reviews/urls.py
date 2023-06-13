from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path(
        '<int:pk>/delete_review/', ReviewDeleteView.as_view(),
        name='delete_review'
        ),
    path('<int:pk>/edit_review/', ReviewUpdateView.as_view(),
         name='edit_review'
         ),
    path('add_review/', ReviewCreateView.as_view(), name='add_review'),
    path('', views.ReviewsList.as_view(), name='reviews'),
]
