from django.urls import path
from .views import checkout, login_view, signup_view , product_list , add_to_cart , cart_view

urlpatterns = [
    path('accounts/login/',login_view , name='login'),
    path('signup/', signup_view, name='signup'),
    path('', product_list, name='home'),
    path('add/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('checkout/', checkout, name='checkout'),
]
