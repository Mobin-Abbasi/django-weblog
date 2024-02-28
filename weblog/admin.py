from django.contrib import admin
from .models import *


# Register your models here.


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 0


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'skills', 'project_completion', 'created', 'updated']
    list_filter = ['skills', 'project_completion', 'created', 'updated']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ['title']}
    raw_id_fields = ['author']
    inlines = [PortfolioImageInline]
