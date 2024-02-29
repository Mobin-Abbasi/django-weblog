from django.urls import path
from . import views

app_name = 'weblog'

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolios', views.portfolio_list, name='portfolio_list'),
    path('portfolios/<pk>', views.portfolio_detail, name='portfolio_detail'),
]