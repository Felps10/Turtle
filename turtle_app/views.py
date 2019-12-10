from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Purchase
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
    products = Product.objects.filter(owner=request.user)
    context = {"products": products}
    return render(request, 'profile.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    purchases = Purchase.objects.filter(product=product.pk)
    context = {"product": product, "purchases": purchases}
    return render(request, 'product_detail.html', context)


def purchase_create(request, pk):
    product = Product.objects.get(id=pk)
    purchase = Purchase(buyer=request.user, product=product)
    purchase.save()
    return redirect('profile')


def cancel_purchase(request, pk):
    product = Product.objects.get(id=pk)


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('product_list')
        else:
            print('error')
    else:
        form = ProductForm()
    context = {'form': form, 'header': "Add New Product"}
    return render(request, 'product_form.html', context)


def product_edit(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product.photo = request.FILES['photo']
            product.save()
            product = form.save()
            return redirect('product_detail', pk=product.pk)
        else:
            print('Form is invalid')
    else:
        form = ProductForm(instance=product)
        context = {'form': form, 'owner': product.owner}
        return render(request, 'product_form.html', context)


def product_delete(request, pk):
    Product.objects.get(id=pk).delete()
    return redirect('profile')
