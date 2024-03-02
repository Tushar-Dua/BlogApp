from django.shortcuts import render
from blog.models import Blog

# Create your views here.


def landing_page(request):
    return render(request, "blog/index.html")


def posts(request):
    context = {'data':Blog.objects.all()}
    return render(request, "blog/all-posts.html",context=context)


def single_post(request, slug):
    return render(request, "blog/post-detail.html" )
