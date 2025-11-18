from django.urls import path
from . import views

app_name = "main" 

urlpatterns = [
    
    path("", views.show_main, name="show_main"),
    path("products/", views.product_list, name="product_list"),
    path("products/<str:id>/", views.show_product, name="show_product"),
    
   
    path("api/products/", views.get_products_ajax, name="get_products_ajax"),
    path("api/products/create/", views.create_product_ajax, name="create_product_ajax"),
    path("api/products/<str:id>/get/", views.get_product_ajax, name="get_product_ajax"),
    path("api/products/<str:id>/update/", views.update_product_ajax, name="update_product_ajax"),
    path("api/products/<str:id>/delete/", views.delete_product_ajax, name="delete_product_ajax"),
    
   
    path('register/', views.register_ajax, name='register'),
    path('login/', views.login_ajax, name='login'),
    path('api/logout/', views.logout_ajax, name='logout_ajax'),
    

    path("products/xml/", views.product_list_xml, name="product_list_xml"),
    path("products/json/", views.product_list_json, name="product_list_json"),
    path("products/<str:id>/xml/", views.product_detail_xml, name="product_detail_xml"),
    path("products/<str:id>/json/", views.product_detail_json, name="product_detail_json"),
    
    
    path("products/add/", views.product_add, name="product_add"),
    path("products/<str:id>/edit/", views.product_edit, name="product_edit"),
    path("products/<str:id>/delete/", views.product_delete, name="product_delete"),
    path('logout/', views.logout_user, name='logout'),
]


#bukin API untuk get product by user, misalkan di access di api/products/user/{id}, 
# nanti dia bakal ngirim json yg isinya product dari user dengan id tersebut


