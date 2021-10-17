from Main.models import Product
from decimal import Decimal

CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        # print('*'*100)
        # print(cart.values())
        # print('*'*100)
        # print(cart)
        for item in cart.values():
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item


    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]= {'quantity':0,'price':str(product.price),'image':'/media/'+str(product.image),'id':product.id}
        self.cart[product_id]['quantity'] += int(quantity)
        self.save()

    def save(self):
        self.session.modified = True
    
    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())   
            

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()

    def quantity_up(self ,item_id):
        self.cart[str(item_id)]['quantity'] += 1
        self.save()

    def quantity_down(self ,item_id):
        self.cart[str(item_id)]['quantity'] -= 1
        self.save()

    # def coupon(self, coupon_discount):
        # self.cart[str(item_id)]['quantity'] -= 1
        # print(self.get_total_price)
        # self.save()