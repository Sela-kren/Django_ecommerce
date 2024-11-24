from django.contrib import admin
from .models import User, Product, ProductTag, ProductTagRelation, Order, OrderItem, ShoppingCart, CartItem, Payment, Review

admin.site.register(User)
admin.site.register(Product)
admin.site.register(ProductTag)
admin.site.register(ProductTagRelation)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShoppingCart)
admin.site.register(CartItem)
admin.site.register(Payment)
admin.site.register(Review)
