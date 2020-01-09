from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import blog


# Create your views here.
class HomeView(ListView):
    model = blog
    template_name = 'index.html'
    context_object_name = "blogs"
    ordering = ['-date']
    paginate_by = 3


class BlogView(DetailView):
    model = blog
    template_name = 'single_post.html'


class CreateBlogView(CreateView):
    model = blog
    template_name = 'create_blog.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# def index(request):
#     return render(request, "index.html")


# def about(request):
#     return render(request, "about.html")