from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
	allblogs = Blog.objects
	return render(request, 'blog/allblogs.html',{'allblogs':allblogs})


def detail(request, id_blog):
	blogpost = get_object_or_404(Blog, pk=id_blog)
	return render(request, 'blog/detail.html', {'blogpost':blogpost}) 