from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Category, BrandCategory
import random
from django.core.mail import send_mail
from django.conf import settings

def contactus(requset):
    send_mail(
    'Subject here',
    'Here is the message.',
    'shoptest20001@gmail.com',
    ['natawe6337@specialistblog.com'],
    fail_silently=False,
)

def index(request):
    home = ''
    r_products = list(Product.objects.all())
    random_items = random.sample(r_products, 3)
    return render(request,'Main/index.html', {'home':home, 'random_items':random_items})

def shop(request, slug=None):
    # return render(request, 'Main/shop.html')
    # print('/*'*100)
    # print(slug)
    shop = ''
    products = Product.objects.all()
    categories = Category.objects.all()
    b_categories = BrandCategory.objects.all()
    if slug:
        print('/*'*100)
        print(slug)
        try:
            category = get_object_or_404(Category, slug=slug)
            products = Product.objects.filter(category = category)
        except:
            b_category = get_object_or_404(BrandCategory, slug=slug)
            products = Product.objects.filter(brand_category = b_category)
    return render(request,'Main/shop.html', {'shop':shop, 'products':products, 'categories':categories,'b_categories':b_categories})

def product_detail(request, slug):
    # product = Product.objects.get(slug = slug)
    product = get_object_or_404(Product, slug = slug)
    return render(request, 'Main/product_detail.html',{'product':product})

def search(request):
    if request.method == 'POST':
        if request.POST['search'] == '':
            products = ''
            return render(request,'Main/search.html',{'products':products})   
        else:
            products = Product.objects.filter(name__contains = request.POST['search'])
            return render(request,'Main/search.html',{'products':products})
    else:
        return redirect('Main:index')