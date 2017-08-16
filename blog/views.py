from django.shortcuts import render
from django.views import generic
from .models import Type, Post, Image
# Create your views here.
class IndexView(generic.ListView):
    model = Type
    context_object_name = 'types'
    template_name = 'blog/type.html'
    def get_queryset(self):
        return Type.objects.all()

class Posts(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/posts.html'

class PostsView(Posts):
    def get_queryset(self):
        return Post.objects.order_by('-published_date')

class PostByTypeView(Posts):
    #is this right? does it ping the database if user enters a post that doesnt exist?
    def get_queryset(self):
        return Post.objects.filter(ptype__posttype=self.kwargs['posttypefilter']).order_by('-published_date')

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/postdetail.html'

class About(generic.ListView):
    model = Type
    context_object_name = 'types'
    template_name = 'blog/about.html'
    def get_queryset(self):
        return Type.objects.all()
