from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Type, Brand
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic


def index(request): 
    return render(request, 'shop/product/index.html')
    
def aboutus(request):
    return render(request, 'shop/product/aboutus.html')

def contactus(request):
    return render(request, 'shop/product/contactus.html')

def privacypolicy(request):
    return render(request, 'shop/product/privacypolicy.html')

#Dynamic Page Views Start Here

def product_list(request, category_slug=None, type_slug = None, brand_slug = None):
    category = None
    categories = Category.objects.all()
    type = None
    types = Type.objects.all()
    brand = None
    brands = Brand.objects.all()

    products = Product.objects.filter(available=True)

    
    

    

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    if type_slug:
        type = get_object_or_404(Type, slug = type_slug)
        products = Product.objects.filter(type=type)
    
    if brand_slug:
        brand = get_object_or_404(Brand, slug = brand_slug)
        products = Product.objects.filter(brand = brand)
    
    paginator = Paginator(products, 8)
    
    page = request.GET.get('page')
 
    try:
        # create Page object for the given page
        products = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        products = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        products = paginator.page(paginator.num_pages)
    
    
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'brand': brand,
        'brands':brands,
        'type': type,
        'types': types,
        
        'products': products
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)