from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('products', views.product_list, name='product_list'),
    path('products/new', views.product_create, name='product_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('profile', views.profile, name='profile')
]
