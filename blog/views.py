from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    #project = Project.objects.all()
    blog = Blog.objects.order_by('-createddatetime') # sorting by latest date
    blog = Blog.objects.order_by('-createddatetime')[:5] # sorting by date & retrieving first 5 items
    # treat this as a python list as objects return a
    # python list. regular python code
    return render(request, "blog/all_blogs.html",{'blogs':blog})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    #return render(request,'blog/detail.html',{'id':blog_id})
    return render(request,'blog/detail.html',{'blog':blog})