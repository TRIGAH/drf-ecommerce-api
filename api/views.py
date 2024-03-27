from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from storeapp.models import Product,Category
from .serializers import CategorySerializer,ProductSerializer
# Create your views here.

@api_view(['GET'])
def api_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def api_product(request,pk):
    product = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def api_category(request):
    categorys = Category.objects.all()
    serializer = CategorySerializer(categorys, many=True)
    return Response(serializer.data, status=200)