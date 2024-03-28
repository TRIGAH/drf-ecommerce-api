from django.urls import path, include
from api import views

urlpatterns = [
    path('products/', views.ApiProducts.as_view()),
    path('products/<str:pk>/', views.api_product),
    path('categorys/', views.api_categorys),
    path('categorys/<str:pk>/', views.api_category),
]