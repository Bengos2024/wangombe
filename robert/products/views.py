from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from .form import ProductForm


def home(request):
    if request.method=='POST':
        data=ProductForm(request.POST)
        if data.is_valid():
            code=request.POST['code']
            name=request.POST['name']
            price=request.POST['price']
            stock=request.POST['stock']
            image_url=request.POST['image_url']
            new_product=Product.objects.create(code=code,name=name,price=price,stock=stock,image_url=image_url)
            new_product.save()
            return HttpResponseRedirect('/')

    product=Product.objects.all()
    form=ProductForm()
    return render(request, "home.html",{'product':product,'form':form})

