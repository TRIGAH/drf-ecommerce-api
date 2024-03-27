from django.urls import path, include
from api import views

urlpatterns = [
    path('products/', views.api_products),
    path('products/<str:pk>/', views.api_product),
    path('categorys/', views.api_categorys),
    path('categorys/<str:pk>/', views.api_category),
]