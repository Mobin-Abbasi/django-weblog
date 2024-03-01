from django import template
from ..models import *

register = template.Library()


@register.inclusion_tag('partials/latest_blog.html')
def latest_blog(count=5):
    l_blog = Blog.objects.order_by('-created')[:count]
    context = {
        'l_blog': l_blog
    }
    return context
