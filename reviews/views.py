from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
from .forms import ReviewForm
# Create your views here.


class ReviewsList(ListView):
    """
    view to Display all the Reviews
    """
    model = Review
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews_list'


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """
    View to Add a Review
    """
    model = Review
    template_name = 'reviews/add_review.html'
    form_class = ReviewForm

    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)