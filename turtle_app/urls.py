from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    # PRODUCTS
    path('products', views.product_list, name='product_list'),
    path('products/new', views.product_create, name='product_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('profile', views.profile, name='profile'),
    # PURCHESES
    path('products/<int:pk>/purchase',
         views.purchase_create, name='purchase_create'),
    path('products/<int:pk>/purchase/delete',
         views.purchase_delete, name='purchase_delete'),
    # SUCCESS PAGE
    path('success', views.success, name='success')
]
