from django.shortcuts import render
from .models import Post, Author

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def posts_by_author(request, author_id):
    author = Author.objects.get(id=author_id)

    posts = Post.objects.filter(author=author)

    return render(request, 'posts_by_author.html', {
        'author': author,
        'posts': posts
    })