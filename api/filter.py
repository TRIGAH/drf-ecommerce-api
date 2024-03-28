from rest_framework import generics
from django_filters import rest_framework as filters
from storeapp.models import Product


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {'category':['exact'], 'old_price':['gte','lte']}