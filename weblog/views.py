from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .forms import *
from django.core.mail import send_mail


# Create your views here.


def index(request):
    portfolios = Portfolio.objects.all()
    blogs = Blog.objects.all()
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = f"{cd['name']}\n{cd['email']}\n\n{cd['comments']}"
            send_mail(cd['subject'], message, 'mobin04dev@gmail.com', ['abbasimobin1383@gmail.com'],
                      fail_silently=False)
    else:
        form = TicketForm()
    context = {
        'portfolios': portfolios,
        'blogs': blogs,
        'form': form,
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
