from django.urls import path
from . import views

app_name = "main" 

urlpatterns = [
    # --- Halaman Utama ---
    path("", views.show_main, name="show_main"),
    path("products/", views.product_list, name="product_list"),

    # --- [PENTING] Path Spesifik (JSON, XML, Add, Flutter) HARUS DI ATAS <str:id> ---
    # Kalau ditaruh di bawah, nanti error lagi karena dikira ID.
    path("products/xml/", views.product_list_xml, name="product_list_xml"),
    path("products/json/", views.product_list_json, name="product_list_json"),
    path("products/add/", views.product_add, name="product_add"),
    path("create-flutter/", views.create_product_flutter, name="create_product_flutter"),
    path("edit-flutter/<str:id>/", views.edit_product_flutter, name="edit_product_flutter"),
    path("delete-flutter/<str:id>/", views.delete_product_flutter, name="delete_product_flutter"),
    path("proxy-image/", views.proxy_image, name="proxy_image"),

    # --- Path Dinamis untuk Detail Produk (Generic) ---
    # Ini ditaruh setelah path spesifik di atas agar aman
    path("products/<str:id>/", views.show_product, name="show_product"),
    
    # Sub-path detail (Edit/Delete/Format khusus per ID)
    path("products/<str:id>/xml/", views.product_detail_xml, name="product_detail_xml"),
    path("products/<str:id>/json/", views.product_detail_json, name="product_detail_json"),
    path("products/<str:id>/edit/", views.product_edit, name="product_edit"),
    path("products/<str:id>/delete/", views.product_delete, name="product_delete"),

    # --- API / AJAX Endpoints ---
    path("api/products/", views.get_products_ajax, name="get_products_ajax"),
    path("api/products/create/", views.create_product_ajax, name="create_product_ajax"),
    
    # [BARU] API Get Product by User ID (Sesuai request Anda)
    path("api/products/user/<int:user_id>/", views.get_products_by_user_id, name="get_products_by_user_id"),

    # API Detail Operations
    path("api/products/<str:id>/get/", views.get_product_ajax, name="get_product_ajax"),
    path("api/products/<str:id>/update/", views.update_product_ajax, name="update_product_ajax"),
    path("api/products/<str:id>/delete/", views.delete_product_ajax, name="delete_product_ajax"),

    # --- Authentication ---
    path("register/", views.register_ajax, name="register"),
    path("login/", views.login_ajax, name="login"),
    path("api/logout/", views.logout_ajax, name="logout_ajax"),
    path("logout/", views.logout_user, name="logout"),
]