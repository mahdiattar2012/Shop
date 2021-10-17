from django.shortcuts import get_object_or_404, redirect, render
from .Cart import Cart
from Main.models import Product
from django.views.decorators.http import require_POST
from django.utils import timezone
from Orders.models import Coupon
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login/')
def detail(request):
    cart = Cart(request)
    return render(request,'Cart/detail.html', {'cart':cart})

@login_required(login_url='/account/login/')
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    rp = request.POST
    try:
        cart.add(product=product, quantity = rp['quantity'])
    except:
        cart.add(product=product, quantity = 1)
    return redirect('Cart:detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    cart.remove(product)
    return redirect('Cart:detail')

def q_up(request, item_id):
    cart = Cart(request)
    cart.quantity_up(item_id=item_id)
    return redirect('Cart:detail')

def q_down(request, item_id):
    cart = Cart(request)
    cart.quantity_down(item_id=item_id)
    return redirect('Cart:detail')

