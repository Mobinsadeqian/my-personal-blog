from django.shortcuts import render, get_object_or_404

from .models import post

def post_list(request):
    posts = post.objects.all().order_by("created_at")
    context = {'posts' : posts}
    
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    mypost = post.objects.get(pk=pk)
    context = {'post' : mypost}
    return render(request, 'blog/post_detail.html',context )

