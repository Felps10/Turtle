from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('products', views.product_list, name='product_list'),
    path('products/new', views.product_create, name='product_create'),
    path('profile', views.profile, name='profile')
]
