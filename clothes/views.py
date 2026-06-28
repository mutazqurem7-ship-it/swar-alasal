from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def offers(request):
    products = Product.objects.all()
    return render(request, 'offers.html', {'products': products})