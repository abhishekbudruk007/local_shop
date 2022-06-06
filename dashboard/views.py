from django.shortcuts import render
from products.models import Product
# Create your views here.

def home(request):
    objects = Product.objects.all() #select*from product
    print('this is home page')
    return render(request, 'dashboard/index.html',context={"products": objects})
def about(request):
    print('this is about page')
    return render(request, 'dashboard/about.html')
