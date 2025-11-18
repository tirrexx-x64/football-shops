from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.contrib.auth.models import User
import requests

# =========================
# Home Page
# =========================
@login_required(login_url='/login')
def show_main(request):
    context = {
        'npm': '2406355621',
        'student_name': request.user.username,
        'student_class': 'PBP C',
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)


# =========================
# Product List Page
# =========================
@login_required(login_url='/login')
def product_list(request):
    context = {
        'app_name': 'Football Shop',
    }
    return render(request, 'products.html', context)


# =========================
# AJAX - Get Products JSON
# =========================
@login_required(login_url='/login')
def get_products_ajax(request):
    filter_type = request.GET.get("filter", "all")
    
    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)
    
    data = []
    for product in products:
        data.append({
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'user': product.user.username if product.user else 'Unknown',
            'is_owner': product.user == request.user,
            'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return JsonResponse({'products': data}, safe=False)


# =========================
# AJAX - Create Product
# =========================
@login_required(login_url='/login')
@csrf_exempt
@require_POST
def create_product_ajax(request):
    try:
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        thumbnail = request.POST.get('thumbnail')
        category = request.POST.get('category')
        is_featured = request.POST.get('is_featured') == 'on'
        stock = request.POST.get('stock')
        brand = request.POST.get('brand')
        
        product = Product.objects.create(
            user=request.user,
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            is_featured=is_featured,
            stock=stock,
            brand=brand
        )
        
        return JsonResponse({
            'status': 'success',
            'message': 'Product created successfully!',
            'product': {
                'id': str(product.id),
                'name': product.name,
                'price': product.price
            }
        }, status=201)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)


# =========================
# AJAX - Update Product
# =========================
@login_required(login_url='/login')
@csrf_exempt
@require_POST
def update_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, id=id)
        
        # Check ownership
        if product.user != request.user:
            return JsonResponse({
                'status': 'error',
                'message': 'You do not have permission to edit this product'
            }, status=403)
        
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.thumbnail = request.POST.get('thumbnail')
        product.category = request.POST.get('category')
        product.is_featured = request.POST.get('is_featured') == 'on'
        product.stock = request.POST.get('stock')
        product.brand = request.POST.get('brand')
        product.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Product updated successfully!',
            'product': {
                'id': str(product.id),
                'name': product.name,
                'price': product.price
            }
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)


# =========================
# AJAX - Delete Product
# =========================
@login_required(login_url='/login')
@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, id=id)
        
        # Check ownership
        if product.user != request.user:
            return JsonResponse({
                'status': 'error',
                'message': 'You do not have permission to delete this product'
            }, status=403)
        
        product_name = product.name
        product.delete()
        
        return JsonResponse({
            'status': 'success',
            'message': f'Product "{product_name}" deleted successfully!'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)


# =========================
# AJAX - Get Single Product
# =========================
@login_required(login_url='/login')
def get_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, id=id)
        
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'user': product.user.username if product.user else 'Unknown',
            'is_owner': product.user == request.user
        }
        
        return JsonResponse({
            'status': 'success',
            'product': data
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=404)


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

def product_list_json_user(request,user_id):
    user = get_object_or_404(User, id=user_id)
    products = Product.objects.filter(user=user)
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
# AJAX - Register
# =========================
@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            
            if password1 != password2:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Passwords do not match!'
                }, status=400)
            
            from django.contrib.auth.models import User
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({
                    'status': 'error',
                    'message': 'Username already exists!'
                }, status=400)
            
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Account created successfully! Please login.'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return render(request, 'register.html')


# =========================
# AJAX - Login
# =========================
@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            response = JsonResponse({
                'status': 'success',
                'message': f'Welcome back, {username}!',
                'username': username
            })
            response.set_cookie('last_login', str(timezone.now()))
            return response
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid username or password!'
            }, status=401)
    
    return render(request, 'login.html')


# =========================
# AJAX - Logout
# =========================
@login_required(login_url='/login')
def logout_ajax(request):
    username = request.user.username
    logout(request)
    response = JsonResponse({
        'status': 'success',
        'message': f'Goodbye, {username}! See you soon.'
    })
    response.delete_cookie('last_login')
    return response


# =========================
# Proxy image endpoint (for Flutter)
# =========================
def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)


# =========================
# KUMPULAN FUNGSI LAMAA
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

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = redirect('main:show_main')
            response.set_cookie('last_login', str(timezone.now()))
            return response
        else:
            messages.error(request, "Username atau password salah.")
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = redirect('main:login')
    response.delete_cookie('last_login')
    return response

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('main:product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if product.user == request.user:
        product.delete()
    return redirect('main:product_list')

@login_required(login_url='/login')
def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    if product.user != request.user:
        return redirect('main:product_list')
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, "product_form.html", {"form": form, "is_edit": True})





def get_products_by_user_id(request, user_id):
    # Mengambil semua produk dimana field 'user' memiliki ID sesuai parameter
    # Jika field di model Product namanya 'author' atau 'owner', ganti 'user__id' jadi 'author__id'
    products = Product.objects.filter(user__id=user_id)
    
    # Mengembalikan data dalam format JSON
    return HttpResponse(serializers.serialize('json', products), content_type="application/json")
