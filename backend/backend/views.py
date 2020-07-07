from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product
from .models import Dependency
from .forms import ProductForm

# HELPERS
# I think eventually we should change this
# If a user creates a product called "This is my product,"
# then the URL would be "/product/This is my product" which
# is very gross. Perhaps add a __str__ function to the Model
# that returns all lowercase string of first word in name?
def retrieve_product(product_name):
    try:
        return Product.objects.get(name=product_name)
    except:    
        return None

def retrieveDependencies (product):
    try:
        return Dependency.objects.filter(dependent=product)
    except:
        return []

# def handle_edit_product(form, name):



### VIEWS ###

def fourohfour(request):
    return render(request, 'fourohfour/fourohfour.html')

# root url is now empty, so redirect to products list view
def temporary_fix(request):
    return HttpResponseRedirect("/products")

def home(request):
    if request.method != 'GET':
        return HttpResponseRedirect("/fourohfour")
    
    page = request.GET.get('page', 1)

    # this is not necessary, this is just to keep consistency
    # that /products alone defaults to page 1
    if page is not None and page == '1':
        return HttpResponseRedirect("/products")

    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
        page = 1
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        page = paginator.num_pages

    context = {
        'products': products,
        'current_page': page,
        'page_range': range(paginator.num_pages)
    }

    return render(request, 'home/index.html', context)



#TODO: 
# 1). Add modals for creating / deleting dependencies
# 2). Add Button + Confirmation modal (i.e. "Are you sure?") for delete product

def product_view(request, name):
    target_product = retrieve_product(name)
    product_dependencies = retrieveDependencies(target_product)
    selected_dep = None
    
    if target_product is None or request.method != 'GET':
        return redirect('/fourohfour')
    else:
        context = {
            'product': target_product,
            'dependencies': product_dependencies,
            'selected_dep': selected_dep
        }
        return render(request, 'home/product_info.html', context)


def product_analytics(request, name):
    target_product = retrieve_product(name)

    if target_product is None or request.method != "GET":
        return redirect('/fourohfour')
    else:
        context = {
            'product': target_product,
            'dependencies': []
        }
        return render(request, 'home/product_analytics.html', context)


def create_product(request):
    return render(request, 'home/test.html', {'req': request})
