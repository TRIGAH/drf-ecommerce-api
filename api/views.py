import uuid
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from storeapp.models import Product,Category
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination 
from django_filters.rest_framework import DjangoFilterBackend
from api.filter import ProductFilter
# Create your views here.

class ProductsViewSet(ModelViewSet):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer  
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['old_price']
    pagination_class = PageNumberPagination

class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
      
            



