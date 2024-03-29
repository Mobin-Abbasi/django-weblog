from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter


# Register your models here.


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 0


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 0


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'skills', 'project_completion', 'created']
    list_filter = ['skills', 'project_completion', ('created', JDateFieldListFilter), ('updated', JDateFieldListFilter)]
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ['title']}
    raw_id_fields = ['author']
    inlines = [PortfolioImageInline]


@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created']
    list_filter = ['category', ('created', JDateFieldListFilter), ('updated', JDateFieldListFilter)]
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ['title']}
    raw_id_fields = ['author']
    inlines = [BlogImageInline]


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created']
