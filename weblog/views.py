from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .forms import *


# Create your views here.


def index(request):
    portfolios = Portfolio.objects.all()
    blogs = Blog.objects.all()
    context = {
        'portfolios': portfolios,
        'blogs': blogs,
    }
    return render(request, 'weblog/index.html', context)


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


def blog_list(request, category=None):
    if category is not None:
        blogs = Blog.objects.filter(category=category)
    else:
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
