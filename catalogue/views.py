from django.shortcuts import render
from django.views import View
from catalogue.models import Product

# Create your views here.

def Products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'base_products.html', context )


class About(View):
    def get(self, request):
       return render(request, 'about.html', {})
    

class Info(View):
    def get(self, request):
       return render(request, 'info.html', {})

class Contacts(View):
    def get(self, request):
       return render(request, 'contacts.html', {})

def LatestPhone(request):
    return render(request, 'latest_phone.html', {})

def UkusedPhones(request):
    return render(request, 'Uk_used_phones.html', {})

def ProductDetails(request, id):
    product_name = Product.objects.get(id=id)
    product = Product.objects.get(product_name=product_name)
    print(product)
    context = {
        'product': product
    }
    return render(request, 'product_details.html', context)