from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# =========================
# Home Page
# =========================
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm': '2406355621',
        'student_name': request.user.username,   # biar sesuai dengan template
        'student_class': 'PBP C',
        'featured_products': product_list,       # sesuaikan dengan template
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)


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
@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, id=id)
    

    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)


# =========================
# Product Add Form
# =========================

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # simpan user yang login
            product.save()
            return redirect('main:product_list')   # pakai namespace
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


# =========================
# Product Delete
# =========================

def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    # hanya pemilik produk yang bisa hapus
    if product.user == request.user:
        product.delete()
    return redirect('main:product_list')   # pakai namespace


# =========================
# Register
# =========================
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created! Please login.')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)


# =========================
# Login
# =========================
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            response = redirect('main:show_main')   # FIX → pakai namespace
            response.set_cookie('last_login', str(timezone.now()))
            return response
        else:
            messages.error(request, "Username atau password salah.")
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login.html', context)


# =========================
# Logout
# =========================
def logout_user(request):
    logout(request)
    response = redirect('main:login')   # pakai namespace
    response.delete_cookie('last_login')
    return response
