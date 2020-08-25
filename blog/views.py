from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def all_blogs(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/index.html', {'posts':posts})

def detail(request, id):
    blog = get_object_or_404(Post, pk=id)
    return render(request, 'blog/detail.html', {"blog":blog})