
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "user"
urlpatterns = [
    path('login',views.login ,name="login"),
    path('auth_user',views.auth_user ,name="auth_user"),
    path('logout',views.logout ,name="logout"),
    path('register', views.register, name="register"),
    path('changepass', views.changepass, name="changepass")
]
