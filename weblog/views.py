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
