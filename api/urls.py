from django.urls import path, include
from api.views import api_products,api_category

urlpatterns = [
    path('product/', api_products),
    path('category/', api_category),
]