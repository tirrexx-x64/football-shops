from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

# =========================
# Home Page
# =========================
def home(request):
    context = {
        'app_name': "Football Shop",
        'student_name': "Tirta Rendy Siahaan",
        'student_class': "PBP C",
        'featured_products': Product.objects.filter(is_featured=True)[:4],
    }
    return render(request, 'main.html', context)


# =========================
# Product List Page
# =========================
def product_list(request):
    context = {
        'products': Product.objects.all(),
        'app_name': 'Football Shop',
    }
    return render(request, 'products.html', context)


# =========================
# Product List XML/JSON
# =========================
def product_list_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products)
    return HttpResponse(data, content_type='application/xml')

def product_list_json(request):
    products = Product.objects.all()
    data = serializers.serialize('json', products)
    return HttpResponse(data, content_type='application/json')


# =========================
# Product Detail XML/JSON by UUID
# =========================
def product_detail_xml(request, id):
    product = get_object_or_404(Product, id=id)
    data = serializers.serialize('xml', [product])
    return HttpResponse(data, content_type='application/xml')

def product_detail_json(request, id):
    product = get_object_or_404(Product, id=id)
    data = serializers.serialize('json', [product])
    return HttpResponse(data, content_type='application/json')


# =========================
# Product Detail Page
# =========================
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})


# =========================
# Product Add Form
# =========================
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list') 
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


# =========================
# Product Delete
# =========================
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')
