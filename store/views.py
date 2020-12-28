from django.shortcuts import render
from store import models


def store(request):
    products = models.Product.objects.all();
    context = {'products':products}
    return render(request,'store/store.html',context)

def cart(request):
    context = {}
    return render(request,'store/cart.html',context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)