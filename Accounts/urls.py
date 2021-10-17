from django.urls import path
from . import views

app_name = 'Accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('activation/', views.activation, name='activation'),
    path('changepassword/', views.change_password, name='change_password'),
    path('forgetpassword/', views.check_email, name='check_email'),
    path('forgetpassword/reset/', views.forget_password, name='forget_password'),
]