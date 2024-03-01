from django.urls import path
from . import views

app_name = 'weblog'

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolios', views.portfolio_list, name='portfolio_list'),
    path('portfolios/<pk>', views.portfolio_detail, name='portfolio_detail'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/category/<str:category>/', views.blog_list, name='blog_list_category'),
    path('blogs/<int:id>/', views.blog_detail, name='blog_detail'),
]