from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Miro S',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2022'
    },
    {
        'author': 'Fantomas',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2022'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})