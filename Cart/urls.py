from django.urls import path
from . import views
app_name = 'Cart'

urlpatterns = [
    path('',views.detail ,name='detail'),
    path('add/<int:product_id>',views.cart_add ,name='cart_add'),
    path('remove/<int:product_id>',views.cart_remove ,name='cart_remove'),
    path('up/<int:item_id>',views.q_up ,name='q_up'),
    path('down/<int:item_id>',views.q_down ,name='q_down'),

]