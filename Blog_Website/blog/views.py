from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_posted']
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post

class EachUserPostsListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/each_post.html'
    ordering = ['-date_posted']
    context_object_name = 'posts'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        cur_post=self.get_object()
        return cur_post.author == self.request.user

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        cur_post=self.get_object()
        return cur_post.author == self.request.user

def about(request):
    return render(request,'blog/about.html',{'title':'About Page'})



