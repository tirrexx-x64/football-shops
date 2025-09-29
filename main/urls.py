from django.urls import path
from . import views
from main.views import register
from main.views import logout_user
from main.views import login_user

app_name = "main" 
urlpatterns = [
    path("", views.show_main, name="show_main"),
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.product_add, name="product_add"),
    path("products/xml/", views.product_list_xml, name="product_list_xml"),
    path("products/json/", views.product_list_json, name="product_list_json"),
    path("products/<str:id>/xml/", views.product_detail_xml, name="product_detail_xml"),
    path("products/<str:id>/json/", views.product_detail_json, name="product_detail_json"),
    path("products/<str:id>/", views.show_product, name="show_product"),
    path("products/<str:id>/delete/", views.product_delete, name="product_delete"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path("products/<str:id>/edit/", views.product_edit, name="product_edit"),

    
]
