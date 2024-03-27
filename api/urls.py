from django.urls import path, include
from api import views

urlpatterns = [
    path('products/', views.api_products),
    path('products/<str:pk>/', views.api_product),
    path('category/', views.api_category),
]