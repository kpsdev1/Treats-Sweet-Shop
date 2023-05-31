from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm


class BlogListView(ListView):
    # view to deisplay reviews
    template_name = 'blog/blog.html'
    model = Post


class BlogDetailView(LoginRequiredMixin, DetailView):
    # display the blog details page

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post.objects, pk=pk)
        comments = post.comments.order_by("-posted_on")
       
        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, pk, *args, **kwargs):
        
        post = get_object_or_404(Post.objects, pk=pk)
        comments = post.comments.order_by("-posted_on")
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your Comment has been Posted')
        else:
            comment_form = CommentForm

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )
        

# #########################################################################
class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    # create a post
    model = Post
    template_name = 'blog/add_post.html'
    form_class = PostForm
    success_message = 'Blog post has been added successfully'

    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    This is the view to edit a review
    """
    model = Post
    template_name = 'blog/edit_post.html'
    form_class = PostForm
    success_message = 'Blog post has been updated successfully'


class BlogDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    This is the view to delete a review
    """
    model = Post
    success_url = reverse_lazy('blog')
    template_name = 'blog/blog.html'
    success_message = 'Blog Post has been deleted'


class CommentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    This is the view to edit a Comment
    """
    model = Comment
    template_name = 'blog/edit_comment.html'
    form_class = CommentForm
    
    def get_success_url(self):
        post = Post.objects.get(pk=self.object.post.pk)
        messages.success(self.request, 'Comment has been Updated!')
        return post.get_absolute_url()

    


class CommentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    This is the view to delete a Comment
    """
    model = Comment

    def get_success_url(self):
        post = Post.objects.get(pk=self.object.post.pk)
        messages.success(self.request, 'Comment has been deleted!')
        return post.get_absolute_url()
        
