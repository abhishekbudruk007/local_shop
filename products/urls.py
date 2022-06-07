
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "products"
urlpatterns = [
    path('product/<int:pk>',views.product_details,name="product"),
    path('wishlist/<int:pk>',views.AddToWishlist, name="add_to_wishlist"),
    path('wishlist',views.WishListView.as_view(), name="wishlist"),
    path('wishlist/<int:pk>/delete', views.delete_wishlist_item, name="delete_from_wishlist" ),
    path('cart_details', views.cart_details, name="cart_details"),
    path('cart_details/<int:pk>/add', views.add_to_cart, name="add_to_cart" ),
    path('cart_details/<int:pk>/reduce', views.reduce_from_cart, name="reduce_from_cart"),
    path('cart_details/<int:pk>/delete', views.remove_from_cart, name="remove_from_cart"),
    path('checkout', views.checkout, name="checkout"),
    # path('about', views.about),
]
