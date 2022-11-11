from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_detail.html'
