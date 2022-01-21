from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from .models import Post


# Create your views here.

# posts = [
#     {
#         'author': 'Shafayet',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'November 17, 2021'
#     },
# {
#         'author': 'Zim',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'November 18, 2021'
#     }
# ]

def home(request):
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# View List
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<view-type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

# View List by specific author
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<view-type>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# View List by specific author
class AuthorPostListView(ListView):
    model = Post
    template_name = 'blog/author_posts.html' # <app>/<model>_<view-type>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# Post Detail
class PostDetailView(DetailView):
    model = Post

# Create Post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # set the author to the current login user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  # validate form

# Update Post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # set the author to the current login user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # checking author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Delete Post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})