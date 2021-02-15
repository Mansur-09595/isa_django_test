from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView

from .models import Post
# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class CreatePostView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class About(TemplateView):
    template_name = 'about.html'