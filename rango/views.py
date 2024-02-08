from django.shortcuts import render
from rango.models import Category
from rango.models import Page

from django.http import HttpResponse

def index(request):
    popular_pages = Page.objects.order_by('-views')[:5]
    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'pages': popular_pages
    }
    return render(request, 'rango/index.html', context=context_dict)



def about(request):
    return render(request, 'rango/about.html', )


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None


    return render(request, 'rango/category.html', context=context_dict)