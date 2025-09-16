from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.product_add, name="product_add"),
    path("products/xml/", views.product_list_xml, name="product_list_xml"),
    path("products/json/", views.product_list_json, name="product_list_json"),
    path("products/<str:id>/xml/", views.product_detail_xml, name="product_detail_xml"),
    path("products/<str:id>/json/", views.product_detail_json, name="product_detail_json"),
    path("products/<str:id>/", views.product_detail, name="product_detail"),
    path("products/<str:id>/delete/", views.product_delete, name="product_delete"),
]
