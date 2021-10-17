from django.urls import path
from . import views

app_name = 'Main'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:slug>', views.shop, name='category_filter'),
    path('shop/<slug:slug>/', views.product_detail, name='product_detail'),
    path('contactus/', views.contactus, name='contactus'),
]