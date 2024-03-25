from django.urls import path, include
from api.views import api_products

urlpatterns = [
    path('product/', api_products),
]