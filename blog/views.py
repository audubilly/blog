from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post



class BlogListView(ListView):
    model = Post
    template_name = 'blog/post_home.html'



class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'



class BlogCreateView(CreateView):
    model = Post
    template_name= 'blog/post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title','body']


class BlogDeleteView(DeleteView):
        model= Post
        template_view= 'blog/post_confirm_delete.html'
        success_url = reverse_lazy('post_home')