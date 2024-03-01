from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'weblog/index.html')


def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios
    }
    return render(request, 'weblog/portfolio_list.html', context)


def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portfolio, id=pk)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'weblog/portfolio_detail.html', context)


def blog_list(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'weblog/blog_list.html', context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    context = {
        'blog': blog,
    }
    return render(request, 'weblog/blog_detail.html', context)
