from django.contrib import admin
from .models import Product,Wishlist,OrderItem,Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(OrderItem)
admin.site.register(Order)
