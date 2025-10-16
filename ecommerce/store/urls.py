from django.urls import path
from store.views import product_list, product_detail, category_list

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('categories/', category_list, name='category-list'),
]