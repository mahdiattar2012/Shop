from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from .models import Coupon, Order, OrderItem
from django.contrib.auth.decorators import login_required
from Cart.Cart import Cart
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib import messages

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    if order.user == request.user:
        return render(request, 'Orders/order.html', {'order':order})
    else:
        return redirect('Main:index')

@login_required
def order_create(request):
    cart = Cart(request)
    if cart.cart == {}:
        messages.error(request,'Your cart is empty')
        return redirect('Cart:detail')
    else:
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order = order, product = item['product'],price = item['price'],quantity = item['quantity'])
        cart.clear()
        return redirect('Orders:detail', order.id)

@require_POST
def coupon_apply(request, order_id):
    now = timezone.now()
    rp = request.POST
    code = rp['code']
    try:
        coupon = Coupon.objects.get(code__exact = code, valid_from__lte = now,valid_to__gte=now,active = True)
        order = Order.objects.get(id = order_id)
        order.discount = coupon.discount
        order.save()
        messages.success(request, 'Your code is correct.')
        return redirect('Orders:detail', order_id)
    except Coupon.DoesNotExist:
        messages.error(request,'This code does not exist')
        return redirect('Orders:detail', order_id)

