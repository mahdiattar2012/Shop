from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Main import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('account/', include('Accounts.urls', namespace='Accounts')),
    path('cart/', include('Cart.urls', namespace='Cart')),
    path('orders/', include('Orders.urls', namespace='Orders')),
    path('contactus/', include('ContactUs.urls', namespace='ContactUs')),
    path('', include('Main.urls', namespace='Main')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
