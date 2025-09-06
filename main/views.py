from django.shortcuts import render
from .models import Product


def home(request):
    # Ganti dengan nama aplikasi dan data diri kamu
    app_name = "Football Shop"
    student_name = "Tirta Rendy Siahaan"   # <-- ganti
    student_class = "PBP C" # <-- ganti

    featured_products = Product.objects.filter(is_featured=True)[:4]

    context = {
        'app_name': app_name,
        'student_name': student_name,
        'student_class': student_class,
        'featured_products': featured_products,
    }
    return render(request, 'main.html', context)


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {
        'products': products,
        'app_name': 'Football Shop'
    })
