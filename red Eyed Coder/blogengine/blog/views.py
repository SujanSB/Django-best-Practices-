from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Tag



# Create your views here.
def posts_list(request):
    posts =Post.objects.all()
    return render(request,'blog/posts_list.html',context={'posts':posts})

def post_detail(request, slug):
    post= Post.objects.get(slug__iexact=slug)
    return render(request,'blog/post_detail.html',context={'post':post})

def tags_list(request):
    tags =Tag.objects.all()
    return render(request,'blog/tags_list.html',context={'tags':tags})

def tag_detail(request):
    tags =Tag.objects.all(slug__iexact=slug)
    return render(request,'blog/tag_detail.html',context={'tag':tag})