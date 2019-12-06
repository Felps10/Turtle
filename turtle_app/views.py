from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

# Create your views here.


def landing(request):
    return render(request, 'landing.html')


def api_products(request):
    all_products = Product.objects.all()
    data = []
    for product in all_products:
        data.append({"name": product.name, "category": product.category,
                     "description": product.description, })
    return JsonResponse({"data": data, "status": 200})


def profile(request):
    return render(request, 'profile.html')


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_list.html', context)


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('landing')
        else:
            print('error')
    else:
        form = ProductForm()
    context = {'form': form, 'header': "Add New Product"}
    return render(request, 'product_form.html', context)
