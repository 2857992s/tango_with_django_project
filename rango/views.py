from django.shortcuts import render,redirect
from django.urls import reverse
from rango.models import Category
from rango.models import Page

from django.http import HttpResponse,HttpRequest
from rango.forms import CategoryForm,PageForm

def index(request):
    popular_categories = Category.objects.all().order_by('-likes')[:5]
    pages = Page.objects.all().order_by('-views')[:5]
    print(popular_categories)

    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'categories': popular_categories,
        'pages': pages
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

def add_category(request:HttpRequest):
    form = CategoryForm()
    if(request.method=='POST'):
        form= CategoryForm(request.POST)
        if form.is_valid() and not Category.objects.all().contains(form):
            form.save(commit=True)
            return redirect('/rango/')
        else:
            print(form.errors)
        
    
    return render(request, 'rango/add_category.html', context={'form':form})

def add_page(request:HttpRequest,category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category=None

    if category is None:
        return redirect('/rango/')

    form = PageForm()

    if(request.method=='POST'):

        form= CategoryForm(request.POST)
        
        if form.is_valid():
            if category:
                page:Page=form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)
        
    context_dict = {'form':form,'category':category}
    return render(request, 'rango/add_page.html', context=context_dict)