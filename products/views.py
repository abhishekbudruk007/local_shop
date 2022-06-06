from django.shortcuts import render, HttpResponse, redirect
from .models import Product,Wishlist
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import traceback
# Create your views here.

def product_details(request,pk):
    product_fetched = Product.objects.filter(id=pk)[0]  #select* from products where id=1,2,3 etc
    context={
        "product":product_fetched
    }
    return render(request, 'products/product_details.html',context)

@login_required
def AddToWishlist(request,pk):
    product_object = Product.objects.filter(id=pk)[0]

    wishlist_object,created=Wishlist.objects.get_or_create(
        wishlist_user=request.user,
        wishlist_product=product_object
    )
    messages.success(request, 'Product added to wishlist')
    return redirect('dashboard:home')

class MyView(LoginRequiredMixin):
    LOGIN_URL = 'login'
    LOGIN_REDIRECT_URL = 'login'


class WishListView(ListView):
    model = Wishlist
    template_name = 'products/wishlist.html'
    context_object_name = "wishlist_objects"
    def get_queryset(self):
        query_set=Wishlist.objects.filter(wishlist_user=self.request.user)# select *from wishlist where user = login_user
        print("queryset", query_set)
        return query_set


def delete_wishlist_item(request, pk):
    print("I am inside delete functionality")
    object = Wishlist.objects.filter(id=pk, wishlist_user=request.user)[0]
    object.delete()
    messages.error(request, "Item from wishlist is deleted successfully")
    # return render(request, 'products/wishlist.html')
    return redirect('products:wishlist')

def wishlist(request):
    wishlist_objects = Wishlist.objects.filter(wishlist_user=request.user)
    return render(request, 'products/wishlist.html', context={"wishlist": wishlist_objects})

from django.utils import timezone
from .models import Order, OrderItem
from django.shortcuts import redirect, get_object_or_404

def cart_details(request):
    # cart_objects = OrderItem.objects.filter(orderitem_user=request.user)
    order_objects = Order.objects.filter(user=request.user, ordered=False)
    print("order_objects", order_objects)
    context = {}
    if order_objects:
        order_objects = order_objects[0]
        context = {
            'order_objects': order_objects
    }

    return render(request, 'products/cart.html', context)


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # product = Product.objects.filter(id=pk)[0]
    order_product, created = OrderItem.objects.get_or_create(
        orderitem_product=product,
        orderitem_user=request.user,
        orderitem_ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.products.filter(orderitem_product__pk=product.pk).exists():
            order_product.orderitem_quantity += 1
            order_product.save()
            messages.info(request, "Added quantity Item")
            return redirect('products:cart_details')
        else:
            order.products.add(order_product)
            messages.info(request, "Item Added to your cart")
            return redirect('products:cart_details')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.products.add(order_product)
        messages.info(request, "Item Added to your cart")
        return redirect('products:cart_details')

def reduce_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(orderitem_product__pk=product.pk).exists():
            order_item = OrderItem.objects.filter(
                orderitem_product=product,
                orderitem_user=request.user,
                orderitem_ordered=False
            )[0]
            if order_item.orderitem_quantity > 1:
                order_item.orderitem_quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("products:cart_details")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("products:cart_details")
    else:
        messages.info(request, "You do not have an order")
        return redirect("products:cart_details")


def remove_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(orderitem_product__pk=product.pk).exists():
            order_item = OrderItem.objects.filter(
                orderitem_product=product,
                orderitem_user=request.user,
                orderitem_ordered=False
            )[0]
            order_item.delete()
            messages.info(request, "Item \"" + order_item.orderitem_product.product_name + "\" removed from your cart")
            return redirect("products:cart_details")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("products:cart_details")
    else:
        messages.info(request, "You do not have an order")
        return redirect("products:cart_details")