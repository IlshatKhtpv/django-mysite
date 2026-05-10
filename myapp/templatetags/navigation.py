from django import template
from myapp.models import Page

register = template.Library()

@register.inclusion_tag('myapp/nav_pages.html')
def show_nav_pages():
    pages = Page.objects.filter(is_visible=True).order_by('order', 'title')
    return {'pages': pages}