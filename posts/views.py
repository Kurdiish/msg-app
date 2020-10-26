from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic import ListView

class HomePage(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'